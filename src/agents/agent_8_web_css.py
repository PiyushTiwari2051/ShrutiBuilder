from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def css_generator_agent(state: AgentState) -> dict:
    """
    Agent 8: Generates professional, highly visual, stunning CSS styles.
    """
    logger.info("Agent 8: CSS Generator Agent started.")
    
    html_code = state.get('html_code', '')
    topic = state.get('topic', '')
    
    llm = get_llm("gemini-2.5-flash")
    parser = StrOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an Elite UI/UX CSS Architect. Create visually stunning, premium, fully responsive CSS3 styles for ShrutiBuilder landing pages. Do not use Tailwind, use pure Vanilla CSS. Incorporate fluid typography, CSS Grid, Flexbox, high-end micro-animations, glowing effects, and glassmorphism styling."),
        ("human", """
        Topic: {topic}
        HTML Structure:
        ```html
        {html}
        ```
        
        Write the complete, modern `style.css` file matching standard classes defined above.
        Requirements:
        1. Fully responsive (mobile, tablet, desktop).
        2. High professional aesthetic (glassmorphism if applicable, nice shadows, smooth gradients).
        3. Do NOT provide HTML/JS. Return ONLY the CSS code.
        4. Use root variables (`:root`) for an incredibly dynamic and modern color palette (e.g. vivid gradients, dark mode default aesthetics).
        5. Provide advanced hover effects, transform micro-animations (scale, translate), glowing neon outlines, and smooth transitions on all interactive elements.
        6. Include media queries for at least 3 breakpoints (mobile, tablet, desktop) ensuring grids stack correctly on small screens.
        7. Use `clamp()` for fluid typography where applicable.
        8. Do not wrap code in ```css .... ``` blocks if possible, just output valid CSS strings.
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "topic": topic,
            "html": html_code[:5000] # Pass first 5000 chars of HTML as context
        })
        
        css_code = response.strip()
        if css_code.startswith("```css"):
            css_code = css_code[6:]
        if css_code.startswith("```"):
            css_code = css_code[3:]
        if css_code.endswith("```"):
            css_code = css_code[:-3]
            
        logger.info(f"Agent 8 generated CSS code ({len(css_code)} characters).")
        return {"css_code": css_code.strip(), "current_agent": "Agent 8"}
    except Exception as e:
        logger.error(f"Agent 8 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 8 Error: {str(e)}"]}
