from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage
from utils.prompts import summarize_prompt
OPENROUTER_API = "openrouter-api-here"

llm = ChatOpenAI(
    openai_api_key=OPENROUTER_API,
    base_url="https://openrouter.ai/api/v1",
    model="google/gemini-2.0-flash-001" #change model as the model used here is a paid llm model
)

def answer_agent(question: str, data: str):
    if not data.strip():
        return "No research data found to answer the question. Please ensure the research agent collected information."

    prompt = PromptTemplate.from_template(summarize_prompt)
    formatted = prompt.format(question=question, data=data)

    try:
        response = llm.invoke([HumanMessage(content=formatted)])
        if response is None or not hasattr(response, "content"):
            return "❌ Model returned an empty response. Please check the model name or try again."
        return response.content
    except Exception as e:
        return f"❌ An error occurred while generating the answer: {str(e)}"
