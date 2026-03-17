def choose_tool(user_input):

    text = user_input.lower()

    if "time" in text:
        return "time"

    if any(char.isdigit() for char in text):
        return "calculator"

    if "what" in text or "who" in text or "explain" in text:
        return "search"

    return "search"