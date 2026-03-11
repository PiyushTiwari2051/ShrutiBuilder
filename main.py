import os
import sys
from dotenv import load_dotenv

# Ensure the root directory is on the path if run standalone
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.graph import create_ppt_generator_graph, create_website_generator_graph
from src.utils.logger import logger

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    load_dotenv()
    clear_screen()
    print("================================================================")
    print("      MULTI-AGENT SHRUTIBUILDER GENERATOR powered by LangGraph")
    print("================================================================\n")
    
    # API Check
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("[!] ERROR: GOOGLE_API_KEY environment variable is not set correctly.")
        print("    Please check your .env file in the root directory and try again.")
        sys.exit(1)
        
    print("What would you like to build?")
    print("  [1] Professional Pitch Deck (PPTX & PDF)")
    print("  [2] Advanced Website (HTML/CSS/JS ZIP)")
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice not in ['1', '2']:
        print("Invalid choice, exiting.")
        sys.exit(1)
        
    build_type = 'ppt' if choice == '1' else 'web'
        
    topic = input("1. Enter ShrutiBuilder Topic / Solution Name: ")
    pdf_path = input("2. Path to ShrutiBuilder Requirement PDF (or enter to skip): ")
    
    slide_limit = None
    if build_type == 'ppt':
        slide_limit_input = input("3. Maximum Slide Limit (optional, press enter to skip): ")
        if slide_limit_input.isdigit():
            slide_limit = int(slide_limit_input)
        instructions = input("4. Any Special Instructions for judging criteria: ")
    else:
        instructions = input("3. Any Special Instructions for design criteria: ")
    
    initial_state = {
        "topic": topic,
        "requirement_pdf_path": pdf_path.strip(),
        "special_instructions": instructions,
        "slide_limit": slide_limit,
        "build_type": build_type,
        "errors": []
    }
    
    print("\n[>>] Compiling Agentic Graph Workflow...\n")
    if build_type == 'ppt':
        app = create_ppt_generator_graph()
    else:
        app = create_website_generator_graph()
    
    print(f"[>>] Dispatching {'Presentation' if build_type == 'ppt' else 'Website'} Agents... (This will take a few minutes)\n")
    try:
        final_state = app.invoke(initial_state)
        
        print("\n========================================================")
        print("                   GENERATION COMPLETE                ")
        print("========================================================\n")
        
        if build_type == 'ppt':
            if final_state.get('pptx_path'):
                print(f"[+] PowerPoint Presentation (.pptx): {final_state['pptx_path']}")
            else:
                print("[!] PPTX generation failed.")
                
            if final_state.get('pdf_path'):
                print(f"[+] PDF Document Export (.pdf): {final_state['pdf_path']}")
            else:
                print("[!] PDF generation failed.")
        else:
            if final_state.get('website_path'):
                print(f"[+] Website Export Folder: {final_state['website_path']}")
            else:
                print("[!] Website generation failed.")
                
            if final_state.get('zip_path'):
                print(f"[+] Full ZIP Download (.zip): {final_state['zip_path']}")
            else:
                print("[!] ZIP generation failed.")
            
        print("\n[i] Agent 12: Quality Review Feedback:")
        feedback = final_state.get('review_feedback', 'No feedback provided.')
        print(f"'{feedback}'")
        
        errors = final_state.get('errors')
        if errors:
            print("\n[!] Execution Warnings:")
            for err in errors[-3:]: # Display only the last 3 errors to prevent spam
                print(f" - {err}")
    
    except Exception as e:
        logger.error(f"Fatal Graph Execution Error: {str(e)}")
        print(f"\n[CRITICAL ERROR] The application encountered a fatal error: {str(e)}")
        
if __name__ == "__main__":
    main()
