from agents.research_agent import research_agent
from agents.answer_agent import answer_agent

def langgraph_flow(query: str) -> str:
    casual_keywords = ["hey", "hi", "hello", "what's up", "how are you"]
    if query.lower().strip() in casual_keywords:
        return "Hey there! 👋 How can I assist you today?"

    # Run research
    data = research_agent(query)
    answer = answer_agent(query, data)
    return answer
