import datetime

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def calculator(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid calculation"

def simple_search(query):
    knowledge_base = {
        "kafka": "Apache Kafka is a distributed event streaming platform used for real-time data pipelines.",
        "kubernetes": "Kubernetes is an open-source platform for managing containerized applications.",
        "python": "Python is a high-level programming language used for backend, AI and automation.",
        "ai agent": "An AI agent is a system that can make decisions and perform tasks using tools and reasoning.",
        "docker": "Docker is a platform used to develop, ship and run applications in containers.",
        "microservices": "Microservices is an architectural style where applications are built as small independent services."
    }

    for key in knowledge_base:
        if key in query.lower():
            return knowledge_base[key]

    return "No information found in local knowledge base."