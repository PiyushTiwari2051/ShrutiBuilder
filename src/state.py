from typing import TypedDict, List, Dict, Any, Optional

class AgentState(TypedDict, total=False):
    """
    State object passed between LangGraph agents.
    Holds all information gathered, generated content, and processing status.
    Uses total=False to allow sparse dictionary initialization.
    """
    # Inputs
    topic: str
    requirement_pdf_path: Optional[str]
    special_instructions: Optional[str]
    slide_limit: Optional[int]
    build_type: str # 'ppt' or 'web'

    # File reading
    pdf_content: str
    
    # Common Agents 1-5
    requirements: Dict[str, Any]
    problem_analysis: Dict[str, Any]
    research_summary: Dict[str, Any]
    solution_structure: Dict[str, Any]
    technical_architecture: Dict[str, Any]
    
    # ------------------
    # PPT Specific States
    # ------------------
    slide_structure: List[Dict[str, Any]]
    slide_content: List[Dict[str, Any]]
    visual_design_guidelines: Dict[str, Any]
    diagrams: Dict[str, str]
    pptx_path: str
    pdf_path: str
    
    # ------------------
    # Web Specific States
    # ------------------
    website_structure: Dict[str, Any]
    html_code: str
    css_code: str
    js_code: str
    website_path: str
    zip_path: str
    
    # ------------------
    # Shared end states
    # ------------------
    review_feedback: str
    quality_passed: bool
    
    # System Control
    current_agent: str
    errors: List[str]
    iteration_count: int
