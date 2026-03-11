from langgraph.graph import StateGraph, END
from src.state import AgentState

# Common Agents
from src.agents.agent_1_requirement import ShrutiBuilder_requirement_analyzer
from src.agents.agent_2_problem import problem_understanding_agent
from src.agents.agent_3_research import research_agent
from src.agents.agent_4_solution import solution_architect_agent
from src.agents.agent_5_technical import technical_architecture_agent

# Web Agents
from src.agents.agent_6_web_structuring import website_structuring_agent
from src.agents.agent_7_web_html import html_generator_agent
from src.agents.agent_8_web_css import css_generator_agent
from src.agents.agent_9_web_js import js_generator_agent
from src.agents.agent_10_web_builder import website_builder_agent
from src.agents.agent_11_web_zip import zip_export_agent
from src.agents.agent_12_web_quality import quality_review_agent as web_quality_review_agent

# PPT Agents
from src.agents.agent_6_ppt_structuring import pitch_deck_structuring_agent
from src.agents.agent_7_ppt_content import slide_content_generator_agent
from src.agents.agent_8_ppt_visual import visual_design_agent
from src.agents.agent_9_ppt_diagram import diagram_generation_agent
from src.agents.agent_10_ppt_builder import ppt_builder_agent
from src.agents.agent_11_ppt_pdf import pdf_export_agent
from src.agents.agent_12_ppt_quality import quality_review_agent_ppt

def _add_common_nodes(workflow):
    workflow.add_node("agent_1_requirements", ShrutiBuilder_requirement_analyzer)
    workflow.add_node("agent_2_problem", problem_understanding_agent)
    workflow.add_node("agent_3_research", research_agent)
    workflow.add_node("agent_4_solution", solution_architect_agent)
    workflow.add_node("agent_5_technical", technical_architecture_agent)

def _add_common_edges(workflow):
    workflow.set_entry_point("agent_1_requirements")
    workflow.add_edge("agent_1_requirements", "agent_2_problem")
    workflow.add_edge("agent_2_problem", "agent_3_research")
    workflow.add_edge("agent_3_research", "agent_4_solution")
    workflow.add_edge("agent_4_solution", "agent_5_technical")


def create_website_generator_graph():
    """Builds the orchestrated workflow for Website Generation."""
    workflow = StateGraph(AgentState)
    _add_common_nodes(workflow)
    
    workflow.add_node("agent_6_web_structuring", website_structuring_agent)
    workflow.add_node("agent_7_web_html", html_generator_agent)
    workflow.add_node("agent_8_web_css", css_generator_agent)
    workflow.add_node("agent_9_web_js", js_generator_agent)
    workflow.add_node("agent_10_web_builder", website_builder_agent)
    workflow.add_node("agent_11_web_zip", zip_export_agent)
    workflow.add_node("agent_12_web_quality", web_quality_review_agent)
    
    _add_common_edges(workflow)
    workflow.add_edge("agent_5_technical", "agent_6_web_structuring")
    workflow.add_edge("agent_6_web_structuring", "agent_7_web_html")
    workflow.add_edge("agent_7_web_html", "agent_8_web_css")
    workflow.add_edge("agent_8_web_css", "agent_9_web_js")
    workflow.add_edge("agent_9_web_js", "agent_10_web_builder")
    workflow.add_edge("agent_10_web_builder", "agent_11_web_zip")
    workflow.add_edge("agent_11_web_zip", "agent_12_web_quality")
    workflow.add_edge("agent_12_web_quality", END)
    
    return workflow.compile()


def create_ppt_generator_graph():
    """Builds the orchestrated workflow for Presentation Generation."""
    workflow = StateGraph(AgentState)
    _add_common_nodes(workflow)
    
    workflow.add_node("agent_6_ppt_structuring", pitch_deck_structuring_agent)
    workflow.add_node("agent_7_ppt_content", slide_content_generator_agent)
    workflow.add_node("agent_8_ppt_visual", visual_design_agent)
    workflow.add_node("agent_9_ppt_diagram", diagram_generation_agent)
    workflow.add_node("agent_10_ppt_builder", ppt_builder_agent)
    workflow.add_node("agent_11_ppt_pdf", pdf_export_agent)
    workflow.add_node("agent_12_ppt_quality", quality_review_agent_ppt)
    
    _add_common_edges(workflow)
    workflow.add_edge("agent_5_technical", "agent_6_ppt_structuring")
    workflow.add_edge("agent_6_ppt_structuring", "agent_7_ppt_content")
    workflow.add_edge("agent_7_ppt_content", "agent_8_ppt_visual")
    workflow.add_edge("agent_8_ppt_visual", "agent_9_ppt_diagram")
    workflow.add_edge("agent_9_ppt_diagram", "agent_10_ppt_builder")
    workflow.add_edge("agent_10_ppt_builder", "agent_11_ppt_pdf")
    workflow.add_edge("agent_11_ppt_pdf", "agent_12_ppt_quality")
    workflow.add_edge("agent_12_ppt_quality", END)
    
    return workflow.compile()
