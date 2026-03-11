from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def website_structuring_agent(state: AgentState) -> dict:
    """
    Agent 6: Generates the website's structure (pages, sections) adapted to the requirements.
    """
    logger.info("Agent 6: Website Structuring Agent started.")
    requirements = state.get('requirements', {})
    
    topic = state.get('topic', '')
    
    llm = get_llm(model_name="gemini-2.5-flash")
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert Website UI/UX Strategist. Determine the exact structure of a high-converting, professional landing page/website."),
        ("human", """
        ShrutiBuilder Topic: {topic}
        
        Create a JSON object detailing the website structure. The object should have a key "pages", which is an array of page objects.
        Since this is usually a single-page scrolling website for a ShrutiBuilder project, you can define the "sections" within the main page.
        
        Example structure:
        {{
            "pages": [
                {{
                    "page_name": "Home",
                    "sections": [
                        {{"section_id": "hero", "title": "Hero Section", "purpose": "Catchy headline and call to action"}},
                        {{"section_id": "problem", "title": "The Problem", "purpose": "Explain what we are solving"}},
                        {{"section_id": "solution", "title": "Our Solution", "purpose": "How our project solves it"}},
                        {{"section_id": "features", "title": "Features", "purpose": "Key technical features"}},
                        {{"section_id": "demo", "title": "Demo/Screenshots", "purpose": "Visual proof"}},
                        {{"section_id": "team", "title": "Team", "purpose": "Who built this"}}
                    ]
                }}
            ]
        }}
        
        Return ONLY valid JSON.
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "topic": topic
        })
        logger.info(f"Agent 6 generated website structure with {len(response.get('pages', []))} pages.")
        return {"website_structure": response, "current_agent": "Agent 6"}
    except Exception as e:
        logger.error(f"Agent 6 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 6 Error: {str(e)}"]}
