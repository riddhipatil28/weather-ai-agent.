from agent.memory import Memory
from agent.tool_registry import ToolRegistry
from agent.executor import Executor
from agent.llm_planner import create_plan
from llm.local_llm import generate_reply
from memory_store.vector_store import VectorMemory


class WeatherAgent:

    def __init__(self, tools_dict):

        # short term memory (chat history)
        self.memory = Memory()

        # long term semantic memory
        self.long_term_memory = VectorMemory()

        # register tools
        self.registry = ToolRegistry()
        for name, func in tools_dict.items():
            self.registry.register(name, func)

        self.executor = Executor(self.registry, self.memory)

    # =====================================
    # HELPER → detect if weather query
    # =====================================
    def is_weather_query(self, message):
        weather_keywords = [
            "weather", "rain", "temperature", "temp",
            "humidity", "forecast", "wind", "sunny",
            "cloud", "snow", "storm"
        ]
        message = message.lower()
        return any(word in message for word in weather_keywords)

    # =====================================
    # MAIN AGENT LOGIC
    # =====================================
    def handle_message(self, message):

        # store user message
        self.memory.add_message("user", message)

        # =====================================
        # SMART MEMORY SEARCH (FAST MODE)
        # =====================================
        short_message = len(message.split()) <= 2

        if short_message:
            past_context = []
        else:
            past_context = self.long_term_memory.search(message)

        # =====================================
        # NORMAL CHAT (NOT WEATHER)
        # =====================================
        if not self.is_weather_query(message):

            reply = generate_reply(
                message,
                tool_results={},
                history=self.memory.get_history(),
                past_context=past_context
            )

            self.memory.add_message("assistant", reply)

            # save meaningful chats only
            if not short_message:
                self.long_term_memory.save(f"USER: {message}")
                self.long_term_memory.save(f"ASSISTANT: {reply}")

            return {
                "reply": reply,
                "trace": "no tools used",
                "memory_recall": past_context
            }

        # =====================================
        # WEATHER QUERY → PLAN + TOOLS
        # =====================================
        planning = create_plan(message)

        tool_results = {}
        for step in planning["plan"]:
            tool_results[step] = self.executor.run(step, message)

        reply = generate_reply(
            message,
            tool_results,
            self.memory.get_history(),
            past_context
        )

        self.memory.add_message("assistant", reply)

        # save meaningful chats only
        if not short_message:
            self.long_term_memory.save(f"USER: {message}")
            self.long_term_memory.save(f"ASSISTANT: {reply}")

        return {
            "reply": reply,
            "trace": planning,
            "memory_recall": past_context
        }
