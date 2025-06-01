from ai_agents.tools.math_tool import math_tool
from langchain.agents import initialize_agent, AgentType
from ai_agents.tools.science_tool import science_tool
from ai_agents.tools.english_tool import english_tool
from ai_agents.tools.history_tool import history_tool
from ai_agents.tools.planner_tool import planner_tool
from ai_agents.tools.retriever_tool import retriever_tool# connects to RAG
from langchain_groq import ChatGroq 
from dotenv import load_dotenv
import os

load_dotenv()


def get_all_tools():
    return [
        retriever_tool(),
        math_tool(),
        science_tool(),
        english_tool(),
        history_tool(),
        planner_tool()
    ]

def run_student_agent(query: str):
    # Initialize LLM
    llm = ChatGroq(
        groq_api_key="groq_api_key",  
        model_name="llama3-70b-8192",
        temperature=0.7
    )  

    # Get tools
    tools = get_all_tools()

    # Initialize agent
    agent = initialize_agent(
        tools=get_all_tools(),
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
    )
