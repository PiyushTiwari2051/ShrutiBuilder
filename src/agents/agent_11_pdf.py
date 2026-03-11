import os
import comtypes.client
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
        return {}

    pdf_path = pptx_path.replace('.pptx', '.pdf')
    
    try:
        # Initialize comtypes server
        comtypes.CoInitialize()
        powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
        # powerpoint.Visible = 1
        
        # Format 32 stands for PDF format in PowerPoint COM
        # https://docs.microsoft.com/en-us/office/vba/api/powerpoint.ppsaveasfiletype
        deck = powerpoint.Presentations.Open(pptx_path, WithWindow=False)
        deck.SaveAs(pdf_path, 32)
        deck.Close()
        powerpoint.Quit()
        comtypes.CoUninitialize()
        
        logger.info(f"Agent 11 exported PDF to {pdf_path}")
        return {"pdf_path": pdf_path, "current_agent": "Agent 11"}
        
    except Exception as e:
        logger.error(f"Failed to export PDF via COM. Is PowerPoint installed? Error: {str(e)}")
        # Provide a fallback logic for non-Windows or machines missing Office
        return {"errors": state.get('errors', []) + [f"Agent 11 PDF Export Error: {str(e)}"]}
