import os
import re
from src.state import AgentState
from src.utils.logger import logger

def clean_filename(name: str) -> str:
    """Removes invalid characters for a folder name."""
    clean = re.sub(r'[^\w\-_\. ]', '_', name)
    return clean.strip()[:50] # Limit length

def website_builder_agent(state: AgentState) -> dict:
    """
    Agent 10: Saves the generated HTML, CSS, and JS to an output directory.
    """
    logger.info("Agent 10: Website Builder Agent started.")
    
    html_code = state.get('html_code', '')
    css_code = state.get('css_code', '')
    js_code = state.get('js_code', '')
    topic = state.get('topic', 'ShrutiBuilder_website')
    
    # Create the target directory inside output folder
    base_output_dir = os.path.join(os.getcwd(), 'output')
    safe_topic_name = clean_filename(topic).replace(" ", "_").lower()
    website_dir = os.path.join(base_output_dir, f"{safe_topic_name}_website")
    
    try:
        os.makedirs(website_dir, exist_ok=True)
        
        # Write files
        html_path = os.path.join(website_dir, 'index.html')
        css_path = os.path.join(website_dir, 'style.css')
        js_path = os.path.join(website_dir, 'script.js')
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_code)
            
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css_code)
            
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js_code)
            
        logger.info(f"Agent 10 successfully wrote website files to: {website_dir}")
        return {"website_path": website_dir, "current_agent": "Agent 10"}
    except Exception as e:
        logger.error(f"Agent 10 failed to write files: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 10 Error: {str(e)}"]}
