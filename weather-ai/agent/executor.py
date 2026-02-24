class Executor:

    def __init__(self, registry, memory):
        self.registry = registry
        self.memory = memory

    def run(self, step, user_message):

        tool = self.registry.get(step)

        if not tool:
            return None

        return tool(user_message, self.memory)
