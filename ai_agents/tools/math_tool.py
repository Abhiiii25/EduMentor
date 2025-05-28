from langchain.tools import Tool

def solve_math_problem(query: str) -> str:
    # Simplified example (can integrate sympy or external APIs)
    if "quadratic" in query:
        return "To factor a quadratic like x² + 5x + 6, find two numbers that multiply to 6 and add to 5: (x+2)(x+3)."
    return "Try to break down the problem. Identify constants and variables."

def math_tool():
    return Tool(
        name="MathHelper",
        func=solve_math_problem,
        description="Use this tool for solving or understanding math problems, especially algebra and geometry."
    )
