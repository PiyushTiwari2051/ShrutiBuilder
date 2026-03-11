import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from src.utils.logger import logger

load_dotenv()

def get_llm(model_name: str = "gemini-2.5-pro", temperature: float = 0.2):
    """
    Factory to retrieve the preferred LLM model (Gemini).
    We use gemini-2.5-pro for advanced professional-grade analysis.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        logger.error("GOOGLE_API_KEY not found in environment!")
        raise ValueError("GOOGLE_API_KEY environment variable is not set. Please check your .env file.")
    
    logger.debug(f"Initializing LLM: {model_name} with temperature {temperature}")
    return ChatGoogleGenerativeAI(
        model=model_name,
        temperature=temperature,
        google_api_key=api_key,
        # Gemini specific setup to avoid common errors:
        max_retries=3
    )

def get_fast_llm():
    """Returns a faster/cheaper model for simple tasks like summarization."""
    return get_llm(model_name="gemini-2.5-flash", temperature=0.2)
