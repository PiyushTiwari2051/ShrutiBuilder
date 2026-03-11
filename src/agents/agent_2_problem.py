from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def problem_understanding_agent(state: AgentState) -> dict:
    """
    Agent 2: Understands the problem deeply, identifies real world use cases, etc.
    """
    logger.info("Agent 2: Problem Understanding Agent started.")
    requirements = state.get('requirements', {})
    topic = state.get('topic', '')
    
    if not requirements or 'problem_statement' not in requirements:
        logger.warning("Agent 2: Missing requirements output. Recovering using raw topic.")
        problem_statement = topic
    else:
        problem_statement = requirements.get('problem_statement', topic)

    llm = get_llm(model_name="gemini-2.5-flash")
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert Product Manager and User Researcher. Analyze the problem deeply and structured."),
        ("human", """
        ShrutiBuilder Problem Statement: {problem}
        
        Analyze this problem and output JSON conforming exactly to instructions.
        Must include:
        - "deep_understanding": string
        - "target_users": list of strings
        - "pain_points": list of strings
        - "real_world_use_cases": list of strings
        - "industry_relevance": string
        
        Format instructions: {format_instructions}
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "problem": problem_statement,
            "format_instructions": parser.get_format_instructions()
        })
        logger.info("Agent 2 completed successfully.")
        return {"problem_analysis": response, "current_agent": "Agent 2"}
    except Exception as e:
        logger.error(f"Agent 2 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 2 Error: {str(e)}"]}
