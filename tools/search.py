from langchain.tools import Tool
from duckduckgo_search import DDGS

def search_duckduckgo(query: str) -> str:
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query)
            top_result = next(results, None)
            
            return top_result["body"] if top_result else "No results found."
    except Exception as e:
        return f"Error: {e}"

def get_search_tool():
    return Tool.from_function(
        name="Search",
        description="Useful for answering questions about current events or unknown topics. Input should be a search query.",
        func=search_duckduckgo
    )
