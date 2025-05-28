from langchain.tools import Tool

def explain_history_event(query: str) -> str:
    if "world war 2" in query.lower():
        return "World War II was a global war from 1939 to 1945 involving most of the world's nations."
    return "Let me explain the historical event or timeline you are asking about."

def history_tool():
    return Tool(
        name="HistoryHelper",
        func=explain_history_event,
        description="Use this tool to explain historical events, dates, or important figures."
    )
