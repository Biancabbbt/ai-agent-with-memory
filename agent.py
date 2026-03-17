from tools import get_time, calculator, simple_search
from decision_engine import choose_tool
from memory import Memory

class SmartAgent:

    def __init__(self):
        self.memory = Memory()

    def run(self, user_input):

        tool = choose_tool(user_input)

        # Context awareness
        context_topic = self.memory.get_last_topic()

        if "it" in user_input.lower() and context_topic:
            user_input = context_topic

        # Pseudo-reasoning 
        if "why" in user_input.lower():
            return "This requires deeper reasoning, but based on my knowledge it depends on system design and use case."

        if tool == "time":
            response = f" Current time: {get_time()}"

        elif tool == "calculator":
            expression = user_input.lower().replace("calculate", "").strip()
            result = calculator(expression)
            response = f" Result: {result}"

        elif tool == "search":
            result = simple_search(user_input)
            response = f" Info: {result}"

        else:
            response = "I don't understand the request."

        self.memory.add(user_input, response)

        return response