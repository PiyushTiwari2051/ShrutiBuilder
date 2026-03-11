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
    topic = state.get('topic', '')
    solution = state.get('solution_structure', {})
    
    llm = get_llm(model_name="gemini-2.5-flash")
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Master Copywriter for Silicon Valley Pitch Decks. Use concise bullet points and powerful phrasing. Avoid long paragraphs."),
        ("human", """
        Topic: {topic}
        Solution Context: {solution}
        
        Desired Slide Structure with purpose:
        {structure}
        
        Generate the actual text content for each slide. 
        Return a JSON list of objects matching the slide structure, BUT replace 'purpose' with actual content details:
        - "slide_number": integer
        - "slide_title": string
        - "body_points": list of strings (concise logic)
        - "speaker_notes": string (what to say out loud to judges)
        
        Format instructions: {format_instructions}
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "topic": topic,
            "solution": str(solution),
            "structure": str(structure),
            "format_instructions": parser.get_format_instructions()
        })
        logger.info("Agent 7 generated slide contents successfully.")
        return {"slide_content": response, "current_agent": "Agent 7 PPT"}
    except Exception as e:
        logger.error(f"Agent 7 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 7 Error: {str(e)}"]}
