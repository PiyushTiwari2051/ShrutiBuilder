from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def visual_design_agent(state: AgentState) -> dict:
    """
    Agent 8: Establishes a visual design guide. Colors, fonts, overall theme.
    """
    logger.info("Agent 8: Visual Design Agent started.")
    topic = state.get('topic', 'General ShrutiBuilder Presentation')
    
    llm = get_llm(model_name="gemini-2.5-flash") # flash is fine for this
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an Elite Presentation Designer. Create a visual identity system for a pitch deck."),
        ("human", """
        ShrutiBuilder Topic / Project Area: {topic}
        
        Output a detailed design JSON object with keys:
        - "theme_name": string
        - "color_palette": list of 4 hex codes (primary, secondary, background, accent)
        - "font_heading": string (standard Google font name)
        - "font_body": string (standard Google font name)
        - "design_style_keywords": list of strings (e.g. ['minimalist', 'neo-brutalism'] or ['clean', 'technological'])
        
        Format instructions: {format_instructions}
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "topic": topic,
            "format_instructions": parser.get_format_instructions()
        })
        logger.info("Agent 8 created visual guidelines successfully.")
        return {"visual_design_guidelines": response, "current_agent": "Agent 8"}
    except Exception as e:
        logger.error(f"Agent 8 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 8 Error: {str(e)}"]}
