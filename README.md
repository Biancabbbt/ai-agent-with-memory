# AI Agent with Memory (Python)

This project implements a simple AI-style agent in Python that simulates how modern AI agents work using tool selection, memory, and context-aware responses.

# Features

- Tool selection based on user input
- Calculator functionality
- Local knowledge-based search
- Time retrieval
- Conversation memory
- Context-aware responses
- Modular architecture

# Architecture

The system is structured into multiple components:

- decision_engine.py → decides which tool to use
- tools.py → contains available tools (search, calculator, time)
- memory.py → stores conversation history
- agent.py → orchestrates agent behavior
- main.py → CLI interface

# Example Usage

You: what is kafka  
Agent: Apache Kafka is a distributed event streaming platform...

You: what is it used for  
Agent: Apache Kafka is a distributed event streaming platform...

You: calculate 10*5  
Agent: Result: 50

# Technologies

- Python
- Modular design
- Rule-based decision system

# How to Run

```bash
py main.py
