import base64
import requests
import os
from src.state import AgentState
from src.utils.llm_factory import get_llm
from src.utils.logger import logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def generate_mermaid_diagram(mermaid_code: str, output_path: str) -> bool:
    """Takes mermaid code, encodes it, fetches from mermaid.ink and saves to PNG."""
    try:
        # Mermaid code must be compact
        graphbytes = mermaid_code.encode("utf-8")
        base64_bytes = base64.urlsafe_b64encode(graphbytes)
        base64_string = base64_bytes.decode("utf-8")
        url = f"https://mermaid.ink/img/{base64_string}?type=png"
        
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            logger.error(f"Mermaid generation failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        logger.error(f"Generate mermaid diagram error: {str(e)}")
        return False

def diagram_generation_agent(state: AgentState) -> dict:
    """
    Agent 9: Generates architecture, workflow, and system diagrams using Mermaid & mermaid.ink
    """
    logger.info("Agent 9: Diagram Generation Agent started.")
    tech_arch = state.get('technical_architecture', {})
    
    llm = get_llm(model_name="gemini-2.5-flash")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert Solutions Architect. Generate valid Mermaid.js graph TD code representing the system architecture. Do not use quotes inside node names, keep it very simple."),
        ("human", """
        Technical Architecture Context:
        {tech_arch}
        
        Output exact Mermaid.js code, nothing else, no markdown code blocks. 
        Start with:
        graph TD
        A[Client/Frontend] --> B[API Gateway]
        ...etc
        """)
    ])
    
    chain = prompt | llm
    
    diagrams_dict = {}
    try:
        response = chain.invoke({"tech_arch": str(tech_arch)})
        mermaid_code = response.content.replace("```mermaid", "").replace("```", "").strip()
        
        output_file = "output/architecture_diagram.png"
        success = generate_mermaid_diagram(mermaid_code, output_file)
        
        if success:
            diagrams_dict['architecture'] = output_file
            logger.info(f"Agent 9: Diagram saved to {output_file}")
        
        return {"diagrams": diagrams_dict, "current_agent": "Agent 9"}
    except Exception as e:
        logger.error(f"Agent 9 failed: {str(e)}")
        return {"errors": state.get('errors', []) + [f"Agent 9 Error: {str(e)}"]}
