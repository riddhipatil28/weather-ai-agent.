import ollama
import json

AVAILABLE_TOOLS = [
    "detect_city",
    "get_weather",
    "predict_temp"
]

def create_plan(user_message):

    prompt = f"""
You are an AI planning system.

User request:
{user_message}

Available tools:
{AVAILABLE_TOOLS}

Return JSON in this format ONLY:

{{
  "intent": "...",
  "reasoning": "...",
  "plan": ["tool1","tool2"]
}}
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {
            "intent": "weather lookup",
            "reasoning": "default fallback",
            "plan": ["detect_city","get_weather"]
        }
