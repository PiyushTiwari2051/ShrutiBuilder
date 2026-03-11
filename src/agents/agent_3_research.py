from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def research_agent(state: AgentState) -> dict:
    """
    Agent 3: Identifies current solutions, competitors, market gap, innovation opportunities.
    """
    logger.info("Agent 3: Research Agent started.")
    problem_analysis = state.get('problem_analysis', {})
    topic = state.get('topic', '')
    
    llm = get_llm(model_name="gemini-2.5-flash")
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert Startup Founder and Market Researcher. Conduct intelligent competitive landscape analysis."),
        ("human", """
        ShrutiBuilder Topic: {topic}
        Problem Analysis Context: {context}
        
        Provide market research output JSON. Follow instructions strictly.
        Must include:
        - "current_solutions": list of strings
        - "competitors": list of strings
        - "market_gaps": list of strings
        - "innovation_opportunities": list of strings
        
        Format instructions: {format_instructions}
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "topic": topic,
            "context": str(problem_analysis),
            "format_instructions": parser.get_format_instructions()
        })
        logger.info("Agent 3 completed successfully.")
        return {"research_summary": response, "current_agent": "Agent 3"}
    except Exception as e:
        logger.error(f"Agent 3 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 3 Error: {str(e)}"]}
