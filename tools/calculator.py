from langchain.tools import Tool
import math

def safe_eval(expression: str) -> str:
    print(f"Evaluating: {expression}")
    
    try:
        return str(eval(expression, {"__builtins__": {}}, math.__dict__))
    except Exception as e:
        return f"Error: {e}"

def get_calculator_tool():
    return Tool.from_function(
        name="Calculator",
        description="Useful for solving math problems. Input should be a valid math expression, like '2 + 2' or 'sqrt(16)'.",
        func=safe_eval
    )
