from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from dotenv import load_dotenv

load_dotenv()


@CrewBase
class MarketResearchCrew:

    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["research_agent"]
        )

    @agent
    def analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["analysis_agent"]
        )

    @agent
    def report_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["report_writer_agent"]
        )

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_research_task"]
        )

    @task
    def market_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_analysis_task"]
        )

    @task
    def final_report_task(self) -> Task:
        return Task(
            config=self.tasks_config["final_report_task"],
            output_file="market_research_report.md"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=False,
            memory=False,
            cache=True
        )