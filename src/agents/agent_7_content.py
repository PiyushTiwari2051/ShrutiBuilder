from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def slide_content_generator_agent(state: AgentState) -> dict:
    """
    Agent 7: Generates professional text per slide. Uses startup pitch language.
    """
    logger.info("Agent 7: Slide Content Generator Agent started.")
    structure = state.get('slide_structure', [])
    
    # Combined context to generate rich content
    context = {
        "topic": state.get('topic'),
        "problem": state.get('problem_analysis'),
        "solution": state.get('solution_structure'),
        "tech": state.get('technical_architecture'),
        "market": state.get('research_summary')
    }
    
    llm = get_llm(model_name="gemini-2.5-flash")
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Master Copywriter for Silicon Valley Pitch Decks. Use concise bullet points and powerful phrasing. Avoid long paragraphs."),
        ("human", """
        Context:
        {context}
        
        Desired Slide Structure with purpose:
        {structure}
        
        Generate the actual text content for each slide. 
        Return a JSON list of objects matching the slide structure, BUT replace 'purpose' with 'content'.
        Each object must have:
        - "slide_number": integer
        - "slide_title": string
        - "body_points": list of strings (3-5 concise bullet points, VERY punchy)
        - "speaker_notes": string (script for the presenter)
        - "suggested_visual_type": string (e.g., 'bulleted', 'diagram', 'chart', 'icon_grid')
        
        Format instructions: {format_instructions}
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "context": str(context),
            "structure": str(structure),
            "format_instructions": parser.get_format_instructions()
        })
        logger.info("Agent 7 generated slide contents successfully.")
        return {"slide_content": response, "current_agent": "Agent 7"}
    except Exception as e:
        logger.error(f"Agent 7 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 7 Error: {str(e)}"]}
