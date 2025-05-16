import warnings
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from tools.calculator import get_calculator_tool

# Suppress the specific LangChain deprecation warning
warnings.filterwarnings("ignore", message=".*LangChain agents will continue to be supported.*")

def create_math_agent():
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini", 
    )

    tools = [get_calculator_tool()]

    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )