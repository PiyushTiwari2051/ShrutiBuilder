from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.pdf_parser import extract_text_from_pdf
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from typing import Dict, Any

def ShrutiBuilder_requirement_analyzer(state: AgentState) -> dict:
    """
    Agent 1: Reads ShrutiBuilder PDF/topic, extracts rules, design criteria, slide limits, etc.
    """
    logger.info("Agent 1: ShrutiBuilder Requirement Analyzer started.")
    topic = state.get('topic', '')
    pdf_path = state.get('requirement_pdf_path', '')
    special_instructions = state.get('special_instructions', '')
    slide_limit = state.get('slide_limit', None)
    build_type = state.get('build_type', 'ppt')
    
    # Extract PDF
    pdf_content = ""
    if pdf_path:
        pdf_content = extract_text_from_pdf(pdf_path)
    
    llm = get_llm(model_name="gemini-2.5-flash")
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert ShrutiBuilder Analyst. Your job is to extract comprehensive rules, judging criteria, problem statement, required sections, and formatting instructions from the provided context.\nOutput exact JSON structure. Do not output anything else."),
        ("human", """
        ShrutiBuilder Topic: {topic}
        Extra Instructions for design: {instructions}
        Slide Limit Preference: {slide_limit}
        Build Type: {build_type}
        
        PDF Content:
        {pdf_content}
        
        Extract the following into a JSON object:
        - "problem_statement": string
        - "slide_limits": integer or null
        - "judging_criteria": list of strings
        - "required_sections": list of strings
        - "formatting_instructions": list of strings
        - "target_audience": string
        
        Format instructions: {format_instructions}
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "topic": topic,
            "instructions": special_instructions,
            "slide_limit": slide_limit,
            "build_type": build_type,
            "pdf_content": pdf_content[:15000],  # Truncate if too large to save tokens
            "format_instructions": parser.get_format_instructions()
        })
        logger.info("Agent 1 completed successfully.")
        return {"requirements": response, "pdf_content": pdf_content, "current_agent": "Agent 1"}
    except Exception as e:
        logger.error(f"Agent 1 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 1 Error: {str(e)}"]}
