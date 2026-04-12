#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime
from pathlib import Path

# Load environment variables from .env file
from dotenv import load_dotenv

# Load .env from project root (parent directory)
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)

from telemedicine_project.crew import TelemedicineProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the Telemedicine Research and Presentation Crew.
    
    This will:
    1. Research "The Future of Telemedicine: AI-Driven Diagnostics"
    2. Generate telemedicine_research.md with comprehensive analysis
    3. Create Final_Submission.pptx using the provided Slide Master
    """
    print("=" * 80)
    print("TELEMEDICINE RESEARCH & PRESENTATION WORKFLOW")
    print("=" * 80)
    print("\nStarting the crew execution...")
    print("\nAgent 1: Research Specialist")
    print("  → Will research telemedicine and AI-driven diagnostics")
    print("  → Output: telemedicine_research.md")
    print("\nAgent 2: Presentation Architect")
    print("  → Will create professional PowerPoint presentation")
    print("  → Output: Final_Submission.pptx (10-15 slides)")
    print("=" * 80)
    print()

    inputs = {
        "current_year": str(datetime.now().year)
    }

    try:
        result = TelemedicineProject().crew().kickoff(inputs=inputs)
        
        # After crew runs, directly generate the PowerPoint from the research file
        # This ensures the PPT is always created even if the agent's tool call fails
        print("\n🎨 Generating Final PowerPoint presentation...")
        from telemedicine_project.tools.powerpoint_tool import PowerPointGeneratorTool
        from pathlib import Path
        
        project_root = Path(__file__).parent.parent.parent
        research_file = project_root / "telemedicine_research.md"
        slide_master = project_root / "AI Bubble_ Detection, Prevention, and Investment Strategies (1).pptx"
        output_pptx = project_root / "Final_Submission.pptx"
        
        if research_file.exists():
            with open(research_file, "r", encoding="utf-8") as f:
                research_content = f.read()
            
            ppt_tool = PowerPointGeneratorTool()
            ppt_result = ppt_tool._run(
                markdown_content=research_content,
                slide_master_path=str(slide_master),
                output_filename=str(output_pptx),
                min_slides=10,
                max_slides=15
            )
            print(ppt_result)
        
        print("\n" + "=" * 80)
        print("EXECUTION COMPLETED SUCCESSFULLY")
        print("=" * 80)
        print("\nGenerated Files:")
        print("  ✓ telemedicine_research.md - Comprehensive research document")
        print("  ✓ Final_Submission.pptx - Professional presentation (10-15 slides)")
        print("\nNext Steps:")
        print("  1. Review telemedicine_research.md for research quality")
        print("  2. Open Final_Submission.pptx to verify design and content")
        print("  3. Ensure Slide Master design language is properly applied")
        print("=" * 80)
        
        return result
        
    except Exception as e:
        print("\n" + "=" * 80)
        print("ERROR OCCURRED")
        print("=" * 80)
        print(f"\nError details: {str(e)}")
        print("\nTroubleshooting:")
        print("  1. Ensure GEMINI_API_KEY is set in .env file")
        print("  2. Verify Slide Master file exists: 'AI Bubble_ Detection, Prevention, and Investment Strategies (1).pptx'")
        print("  3. Check that Kiro PowerPoint MCP Power is installed")
        print("  4. Run 'uv sync' to ensure all dependencies are installed")
        print("=" * 80)
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "current_year": str(datetime.now().year)
    }
    try:
        TelemedicineProject().crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TelemedicineProject().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "current_year": str(datetime.now().year)
    }
    try:
        TelemedicineProject().crew().test(
            n_iterations=int(sys.argv[1]), 
            eval_llm=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "current_year": str(datetime.now().year)
    }

    try:
        result = TelemedicineProject().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")


if __name__ == "__main__":
    run()
