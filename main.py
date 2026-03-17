from agent import SmartAgent

agent = SmartAgent()

print("Smart AI Agent started (type exit to stop)")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    response = agent.run(user_input)

    print("Agent:", response)