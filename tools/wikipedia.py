from langchain.tools import Tool
import wikipedia

def wiki_search(query: str) -> str:
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception as e:
        return f"Error: {e}"

def get_wikipedia_tool():
    return Tool.from_function(
        name="Wikipedia",
        description="Useful for getting summaries of factual topics from Wikipedia. Input should be a topic name, like 'Mars' or 'World War 2'.",
        func=wiki_search
    )
