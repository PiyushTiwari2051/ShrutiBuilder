from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def js_generator_agent(state: AgentState) -> dict:
    """
    Agent 9: Generates functional, animated, or interactive JS code.
    """
    logger.info("Agent 9: JS Generator Agent started.")
    
    html_code = state.get('html_code', '')
    css_code = state.get('css_code', '')
    topic = state.get('topic', '')
    
    llm = get_llm("gemini-2.5-flash")
    parser = StrOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an Elite Javascript Developer specializing in highly interactive, premium web experiences. Create engaging, bug-free, modern Javascript code to handle interactivity on a ShrutiBuilder solution's landing page."),
        ("human", """
        Topic: {topic}
        HTML Snippet:
        ```html
        {html}
        ```
        
        Write the complete `script.js` file for the above webpage.
        Requirements:
        1. Add event listeners like smooth scrolling, navigation bar toggling, sticky headers.
        2. Incorporate scroll animations (e.g. reveal on scroll) using IntersectionObserver if suitable.
        3. Do NOT provide HTML/CSS. Return ONLY the JS code.
        4. Validate basic form inputs if a contact/auth form exists.
        5. Add highly advanced custom interactions, like cursor-following glows, 3D tilt effects on cards, or parallax data elements.
        6. Use ES6+ syntax gracefully. Include modular closures (IIFE) if required to prevent polluting global scope.
        7. Return only valid vanilla JS code. Do not wrap in markdown blocks like ```javascript or ```; just return plain text Javascript code.
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "topic": topic,
            "html": html_code[:3000] # Provide HTML context for class ID names
        })
        
        js_code = response.strip()
        if js_code.startswith("```javascript"):
            js_code = js_code[13:]
        if js_code.startswith("```js"):
            js_code = js_code[5:]
        if js_code.startswith("```"):
            js_code = js_code[3:]
        if js_code.endswith("```"):
            js_code = js_code[:-3]
            
        logger.info(f"Agent 9 generated JS code ({len(js_code)} characters).")
        return {"js_code": js_code.strip(), "current_agent": "Agent 9"}
    except Exception as e:
        logger.error(f"Agent 9 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 9 Error: {str(e)}"]}
