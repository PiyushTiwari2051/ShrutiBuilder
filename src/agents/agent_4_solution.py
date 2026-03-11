from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def solution_architect_agent(state: AgentState) -> dict:
    """
    Agent 4: Designs the best possible solution ensuring innovation, feasibility, scalability, and uniqueness.
    """
    logger.info("Agent 4: Solution Architect Agent started.")
    problem = state.get('problem_analysis', {})
    research = state.get('research_summary', {})
    
    llm = get_llm(model_name="gemini-2.5-flash")
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an Elite Solution Architect for ShrutiBuilder winning products. Formulate the core offering."),
        ("human", """
        Based on Problem: {problem}
        And Market Context: {research}
        
        Design an innovative, highly feasible, scalable, and unique product solution.
        Must output JSON conforming strictly to instructions with keys:
        - "core_solution": string
        - "key_features": list of strings (at least 3-5)
        - "innovation_factor": string
        - "feasibility_plan": string
        - "scalability_approach": string
        - "unique_value_proposition": string
        
        Format instructions: {format_instructions}
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "problem": str(problem),
            "research": str(research),
            "format_instructions": parser.get_format_instructions()
        })
        logger.info("Agent 4 completed successfully.")
        return {"solution_structure": response, "current_agent": "Agent 4"}
    except Exception as e:
        logger.error(f"Agent 4 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 4 Error: {str(e)}"]}
