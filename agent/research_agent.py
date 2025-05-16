import warnings
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from tools.wikipedia import get_wikipedia_tool
from tools.search import get_search_tool
from dotenv import load_dotenv

# Suppress the specific LangChain deprecation warning
warnings.filterwarnings("ignore", message=".*LangChain agents will continue to be supported.*")

load_dotenv()

def create_research_agent():
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini", 
    )

    tools = [get_wikipedia_tool(), get_search_tool()]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent
