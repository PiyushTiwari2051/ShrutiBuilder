from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def pitch_deck_structuring_agent(state: AgentState) -> dict:
    """
    Agent 6: Generates the actual slide structure adapted to the requirements.
    """
    logger.info("Agent 6: Pitch Deck Structuring Agent started.")
    requirements = state.get('requirements', {})
    
    # Optional logic from requirements
    slide_limits = requirements.get('slide_limits') or state.get('slide_limit')
    required_sections = requirements.get('required_sections', [])
    topic = state.get('topic', '')
    
    llm = get_llm(model_name="gemini-2.5-flash")
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert Pitch Deck Strategist. Determine the exact sequence of slides for a ShrutiBuilder presentation."),
        ("human", """
        ShrutiBuilder Topic: {topic}
        Preferred Max Slides: {slide_limits}
        Required Sections by judges: {required_sections}
        
        Create a JSON array of slide objects. Each object must have:
        - "slide_number": integer
        - "slide_title": string
        - "purpose": string
        
        If slide_limits is provided, do NOT exceed that number of slides.
        Include required sections naturally. Make it flow logically.
        Format instructions: {format_instructions}
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "topic": topic,
            "slide_limits": slide_limits if slide_limits else 'No strict limit, usually 10-15',
            "required_sections": required_sections,
            "format_instructions": parser.get_format_instructions()
        })
        logger.info(f"Agent 6 generated {len(response)} slides in structure.")
        return {"slide_structure": response, "current_agent": "Agent 6 PPT"}
    except Exception as e:
        logger.error(f"Agent 6 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 6 Error: {str(e)}"]}
