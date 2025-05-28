from langchain.tools import Tool

def explain_science_concept(query: str) -> str:
    if "photosynthesis" in query.lower():
        return "Photosynthesis is the process by which green plants use sunlight to make food from carbon dioxide and water."
    return "Let's break the science concept into simpler parts. Can you specify the topic?"

def science_tool():
    return Tool(
        name="ScienceHelper",
        func=explain_science_concept,
        description="Use this tool to explain science concepts like biology, chemistry, or physics."
    )
