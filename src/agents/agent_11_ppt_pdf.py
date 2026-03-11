import os
import time
from src.state import AgentState
from src.utils.logger import logger

def pdf_export_agent(state: AgentState) -> dict:
    """
    Agent 11: Converts PPT into PDF format using comtypes on Windows.
    """
    logger.info("Agent 11: PDF Export Agent started.")
    pptx_path = state.get('pptx_path')
    
    if not pptx_path or not os.path.exists(pptx_path):
        logger.error("PPTX path not found for PDF conversion.")
        return {"errors": state.get('errors', []) + ["Agent 11: PPTX not found."]}
        
    if not pptx_path.endswith('.pptx'):
        return {"errors": state.get('errors', []) + ["Agent 11: Invalid PPTX file extension."]}
        
    pdf_path = pptx_path.replace('.pptx', '.pdf')
    
    try:
        import comtypes.client
        # Avoid permission issues and instance locking
        powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
        powerpoint.Visible = 1
        
        # Open Presentation silently
        deck = powerpoint.Presentations.Open(pptx_path, WithWindow=False)
        
        # Save As PDF (format type 32)
        deck.SaveAs(pdf_path, 32)
        deck.Close()
        powerpoint.Quit()
        
        logger.info(f"Agent 11 successfully created PDF: {pdf_path}")
        return {"pdf_path": pdf_path, "current_agent": "Agent 11 PPT"}
        
    except Exception as e:
        logger.error(f"Agent 11 PDF Export Error: {str(e)}")
        # If comtypes fails (e.g., no PowerPoint installed on system)
        return {"errors": state.get('errors', []) + [f"Agent 11 (PDF Export) Error: {str(e)}"]}
