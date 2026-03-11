from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def html_generator_agent(state: AgentState) -> dict:
    """
    Agent 7: Generates semantic HTML5 matching the Website Structure.
    It leaves classes/IDs ready for styling with modern CSS and interaction with JS.
    """
    logger.info("Agent 7: HTML Generator Agent started.")
    
    website_structure = state.get('website_structure', {})
    topic = state.get('topic', '')
    solution = state.get('solution_structure', {})
    
    llm = get_llm(model_name="gemini-2.5-flash")
    parser = StrOutputParser()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an Elite Frontend Developer. Generate a highly structured, scalable, accessible, and semantic HTML5 code. This is for an advanced, professional ShrutiBuilder website. Ensure the document structure allows for deeply responsive CSS and interactive JS."),
        ("human", """
        Topic: {topic}
        Website Structure Planned: {structure}
        Solution Context: {solution}
        
        Write the complete, semantic HTML structure.
        - DO NOT provide CSS (that comes later). Let the HTML have descriptive classes/IDs (e.g. `section-hero`, `feature-card`, `btn-primary`, etc.).
        - DO NOT wrap the output in Markdown blocks like ```html .... ```. Give me ONLY the clean HTML string or if you use blocks, I'll extract it, but preferably just output plain text HTML starting with <!DOCTYPE html>.
        - DO NOT provide JS inline.
        - The `body` element should include all structured sections mentioned above.
        - Provide rich textual content based on the Topic and Solution. Do not just use Lorem Ipsum.
        - Link to an external stylesheet called `style.css`.
        - Link to an external script called `script.js` at the end of the body.
        - Include meta viewport tags to ensure full mobile responsiveness.
        - Include modern elements with deep nesting classes (e.g., containers, wrappers, grids, flex containers) for ultra-advanced CSS styling.
        - Include Google Fonts (e.g. 'Inter' or 'Poppins') and FontAwesome CDN links in the `<head>` to allow for modern typography and iconography.
        - Use modern semantic tags (<header>, <nav>, <section>, <article>, <footer>, <main>).
        """)
    ])
    
    chain = prompt | llm | parser
    
    try:
        response = chain.invoke({
            "topic": topic,
            "structure": website_structure,
            "solution": solution
        })
        
        # Clean up markdown code blocks if the LLM provided them
        html_code = response.strip()
        if html_code.startswith("```html"):
            html_code = html_code[7:]
        if html_code.startswith("```"):
            html_code = html_code[3:]
        if html_code.endswith("```"):
            html_code = html_code[:-3]
        
        logger.info(f"Agent 7 generated HTML code ({len(html_code)} characters).")
        return {"html_code": html_code.strip(), "current_agent": "Agent 7"}
    except Exception as e:
        logger.error(f"Agent 7 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 7 Error: {str(e)}"]}
