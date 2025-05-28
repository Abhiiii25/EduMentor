from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from langchain_core.tools import Tool
from ai_agents.tools.retriever_tool import retriever_tool
from ai_agents.tools.math_tool import math_tool
from ai_agents.tools.planner_tool import planner_tool
from ai_agents.memory.memory_manager import get_memory

llm = ChatGroq(temperature=0.7, model_name="llama3-70b-8192")

tools = [
    retriever_tool(),
    math_tool(),
    planner_tool(),
]

memory = get_memory()

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
    handle_parsing_errors=True
)

def run_agent(query):
    return agent.run(query)
