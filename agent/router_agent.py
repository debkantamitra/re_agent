from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from agent.math_agent import create_math_agent
from agent.research_agent import create_research_agent

def create_router_agent():
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

    math_agent = create_math_agent()
    research_agent = create_research_agent()    

    def route_input(user_input: str) -> str:
        prompt = PromptTemplate.from_template("""
You are a router assistant.
Decide if the user query is more about:
- MATH (numbers, calculations, math expressions)
- RESEARCH (facts, events, general knowledge)

Return just one word: MATH or RESEARCH.

Query: {query}
Answer:""")

        formatted_prompt = prompt.format_prompt(query=user_input).to_string()

        # Proper usage with ChatOpenAI expects a list of messages
        response = llm([HumanMessage(content=formatted_prompt)])
        decision = response.content.strip().upper()

        if "MATH" in decision:
            return math_agent.run(user_input)
        else:
            return research_agent.run(user_input)

    return route_input
