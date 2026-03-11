import pdfplumber
from src.utils.logger import logger
import os

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts text content from a ShrutiBuilder requirement PDF."""
    if not pdf_path or not os.path.exists(pdf_path):
        logger.warning(f"PDF path invalid or empty: {pdf_path}")
        return ""
        
    text_content = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_content.append(page_text)
        logger.info(f"Successfully extracted {len(text_content)} pages from {pdf_path}")
        return "\n\n".join(text_content)
    except Exception as e:
        logger.error(f"Failed to extract text from {pdf_path}: {str(e)}")
        return ""
