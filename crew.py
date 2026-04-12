from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, FileReadTool
from telemedicine_project.tools.powerpoint_tool import create_powerpoint_tool
import os
from pathlib import Path

# Resolve absolute paths relative to project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
SLIDE_MASTER_PATH = str(PROJECT_ROOT / "AI Bubble_ Detection, Prevention, and Investment Strategies (1).pptx")
RESEARCH_FILE_PATH = str(PROJECT_ROOT / "telemedicine_research.md")
OUTPUT_PPTX_PATH = str(PROJECT_ROOT / "Final_Submission.pptx")


@CrewBase
class TelemedicineProject():
    """Telemedicine Research and Presentation Crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["research_specialist"],  # type: ignore[index]
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def presentation_architect(self) -> Agent:
        return Agent(
            config=self.agents_config["presentation_architect"],  # type: ignore[index]
            tools=[
                FileReadTool(),
                create_powerpoint_tool(),
            ],
            verbose=True,
        )

    @task
    def telemedicine_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["telemedicine_research_task"],  # type: ignore[index]
        )

    @task
    def presentation_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config["presentation_creation_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Telemedicine Research and Presentation Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
