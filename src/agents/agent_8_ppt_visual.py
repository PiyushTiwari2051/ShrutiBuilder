from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def visual_design_agent(state: AgentState) -> dict:
    """
    Agent 8: Determines color palettes, fonts, and visual theme based on the topic.
    """
    logger.info("Agent 8: Visual Design Agent started.")
    topic = state.get('topic', 'General ShrutiBuilder Presentation')
    
    llm = get_llm(model_name="gemini-2.5-flash")
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an Elite Presentation Designer. Create a visual identity system for a pitch deck."),
        ("human", """
        Topic: {topic}
        
        Define visually appealing, modern, startup-style theme constraints.
        Must return JSON:
        - "primary_color": string (HEX)
        - "secondary_color": string (HEX)
        - "background_color": string (HEX, prefer dark modern schemes or clean white)
        - "font_family": string (e.g. 'Arial', 'Calibri')
        - "visual_theme_description": string
        
        Format instructions: {format_instructions}
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "topic": topic,
            "format_instructions": parser.get_format_instructions()
        })
        logger.info("Agent 8 generated visual guidelines.")
        return {"visual_design_guidelines": response, "current_agent": "Agent 8 PPT"}
    except Exception as e:
        logger.error(f"Agent 8 failed: {str(e)}")
        # Provide safe fallback
        return {
            "visual_design_guidelines": {
                "primary_color": "#0F52BA",
                "secondary_color": "#FFC000",
                "background_color": "#FFFFFF",
                "font_family": "Calibri",
                "visual_theme_description": "Clean corporate default."
            },
            "errors": state.get('errors', []) + [f"Agent 8 Error: {str(e)}"]
        }
