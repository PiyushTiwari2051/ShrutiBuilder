from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def quality_review_agent(state: AgentState) -> dict:
    """
    Agent 12: Evaluates the generated HTML, CSS, and JS components against the original requirements.
    QA process.
    """
    logger.info("Agent 12: Quality Review Agent started.")
    requirements = state.get('requirements', {})
    
    html_code = state.get('html_code', '')
    css_code = state.get('css_code', '')
    js_code = state.get('js_code', '')
    
    llm = get_llm(model_name="gemini-2.5-flash")
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an Elite QA Software Tester and UI/UX Evaluator. Evaluate the generated website files."),
        ("human", """
        Requirements: {requirements}
        
        Evaluated code snippets (limited for context):
        HTML Length: {html_len} characters
        CSS Length: {css_len} characters
        JS Length: {js_len} characters
        
        Review for formatting requirements, storytelling, professional quality, responsive design logic, and structural completeness based on typical ShrutiBuilder website standards.
        Output exact JSON:
        - "feedback": string (brief summary)
        - "passed": boolean
        - "suggested_changes": list of strings (what should be improved next time)
        
        Format instructions: {format_instructions}
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "requirements": str(requirements)[:1000],
            "html_len": len(html_code),
            "css_len": len(css_code),
            "js_len": len(js_code),
            "format_instructions": parser.get_format_instructions()
        })
        logger.info(f"Agent 12 review completed. Passed: {response.get('passed')}")
        return {
            "review_feedback": response.get('feedback', ''),
            "quality_passed": response.get('passed', True),
            "current_agent": "Agent 12"
        }
    except Exception as e:
        logger.error(f"Agent 12 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 12 Error: {str(e)}"]}
