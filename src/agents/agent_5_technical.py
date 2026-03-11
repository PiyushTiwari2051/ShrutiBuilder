from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def technical_architecture_agent(state: AgentState) -> dict:
    """
    Agent 5: Designs system architecture, tech stack, AI components, APIs, and workflow.
    """
    logger.info("Agent 5: Technical Architecture Agent started.")
    solution = state.get('solution_structure', {})
    
    llm = get_llm(model_name="gemini-2.5-flash")
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Chief Technology Officer (CTO). Define the tech stack, system architecture, and workflows for the product."),
        ("human", """
        Solution Context: {solution}
        
        Provide the technical JSON specifications conforming strictly to instructions.
        Keys must include:
        - "frontend_stack": list of strings
        - "backend_stack": list of strings
        - "ai_components": list of strings
        - "database_cloud": list of strings
        - "api_architecture": string
        - "development_workflow": string
        
        Format instructions: {format_instructions}
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "solution": str(solution),
            "format_instructions": parser.get_format_instructions()
        })
        logger.info("Agent 5 completed successfully.")
        return {"technical_architecture": response, "current_agent": "Agent 5"}
    except Exception as e:
        logger.error(f"Agent 5 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 5 Error: {str(e)}"]}
