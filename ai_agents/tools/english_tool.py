from langchain.tools import Tool

def explain_english_concept(query: str) -> str:
    if "simile" in query.lower():
        return "A simile is a figure of speech comparing two different things using 'like' or 'as'."
    return "Let me help with your grammar or literature question."

def english_tool():
    return Tool(
        name="EnglishHelper",
        func=explain_english_concept,
        description="Use this tool for grammar help, literary terms, and writing tips."
    )
