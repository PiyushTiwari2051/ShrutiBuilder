import os
import shutil
from src.state import AgentState
from src.utils.logger import logger

def zip_export_agent(state: AgentState) -> dict:
    """
    Agent 11: Zips the created website folder into a downloadable archive.
    """
    logger.info("Agent 11: ZIP Export Agent started.")
    
    website_dir = state.get('website_path')
    
    if not website_dir or not os.path.isdir(website_dir):
        msg = "Agent 11 Error: Valid Website Directory not found to zip."
        logger.error(msg)
        return {"errors": state.get('errors', []) + [msg]}
        
    try:
        # We will create a zip file with the same name as the folder
        zip_path = shutil.make_archive(
            base_name=website_dir,
            format='zip',
            root_dir=website_dir
        )
        
        logger.info(f"Agent 11 successfully created ZIP archive: {zip_path}")
        return {"zip_path": zip_path, "current_agent": "Agent 11"}
        
    except Exception as e:
        logger.error(f"Agent 11 failed to create ZIP: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 11 Error: {str(e)}"]}
