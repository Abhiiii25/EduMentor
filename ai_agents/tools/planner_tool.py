from langchain.tools import Tool

def suggest_study_plan(query: str) -> str:
    return (
        "Based on your test next week, here’s a plan:\n"
        "- Day 1: Review key concepts\n"
        "- Day 2: Practice problems\n"
        "- Day 3: Mock test\n"
        "- Day 4: Revise mistakes\n"
        "- Day 5: Final brush-up"
    )

def planner_tool():
    return Tool(
        name="StudyPlanner",
        func=suggest_study_plan,
        description="Use this tool to get a 5-day personalized study plan."
    )
