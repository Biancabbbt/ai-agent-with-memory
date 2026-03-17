class Memory:

    def __init__(self):
        self.history = []

    def add(self, user_input, response):
        self.history.append({
            "user": user_input,
            "response": response
        })

    def get_last_topic(self):
        if not self.history:
            return None

        last = self.history[-1]["user"].lower()

        for topic in ["kafka", "kubernetes", "python", "docker", "microservices"]:
            if topic in last:
                return topic

        return None