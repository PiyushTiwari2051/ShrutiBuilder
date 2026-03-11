from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def quality_review_agent_ppt(state: AgentState) -> dict:
    """
    Agent 12 (PPT): Verifies if the requirements are met in the slide content.
    """
    logger.info("Agent 12: PPT Quality Review Agent started.")
    requirements = state.get('requirements', {})
    slide_content = state.get('slide_content', [])
    
    llm = get_llm(model_name="gemini-2.5-flash")
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an Elite QA Editor and Pitch Coach. Evaluate the generated slide deck content."),
        ("human", """
        Requirements: {requirements}
        
        Slide Deck Content:
        {slide_content}
        
        Review for formatting requirements, storytelling, professional quality, and coverage.
        Output exact JSON:
        - "feedback": string
        - "passed": boolean
        - "suggested_changes": list of strings
        
        Format instructions: {format_instructions}
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "requirements": str(requirements),
            "slide_content": str(slide_content),
            "format_instructions": parser.get_format_instructions()
        })
        logger.info(f"Agent 12 PPT review completed. Passed: {response.get('passed')}")
        return {
            "review_feedback": response.get('feedback', ''),
            "quality_passed": response.get('passed', True),
            "current_agent": "Agent 12 PPT"
        }
    except Exception as e:
        logger.error(f"Agent 12 PPT failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 12 PPT Error: {str(e)}"]}
