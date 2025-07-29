from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool , ScrapeWebsiteTool , FileWriterTool
from dotenv import load_dotenv
from crewai.llm import LLM
#from crewai.llms import LLM 
import os

load_dotenv()  

llm = LLM(
    provider="google",
    model=os.getenv("MODEL", "gemini-pro"),
    api_key=os.getenv("GOOGLE_API_KEY") 
)





load_dotenv()


@CrewBase
class AiNewsScraper():
    """AiNewsScraper crew"""
    agents_config = 'config/agents.yaml'
    tasks_config =  'config/tasks.yaml'

    @agent
    def retrive_news(self) -> Agent:
        return Agent(
            config=self.agents_config['retrive_news'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def Website_scrapper(self) -> Agent:
        return Agent(
            config=self.agents_config['Website_scrapper'], 
            tools=[ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def ai_news_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_news_writer'], 
            tools=[],
            verbose=True
        )
    @agent
    def File_saver(self) -> Agent:
        return Agent(
            config=self.agents_config['File_saver'], 
            tools=[FileWriterTool()],
            verbose=True
        )



    @task
    def retrive_news_task(self) -> Task:
        return Task(
            config=self.tasks_config['retrive_news_task'] )

    @task
    def Website_scrapper_task(self) -> Task:
        return Task(
            config=self.tasks_config['Website_scrapper_task']
        )
    @task
    def ai_news_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['ai_news_writer_task']
        )
    @task
    def File_saver_task(self) -> Task:
        return Task(
            config=self.tasks_config['File_saver_task']
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the AiNewsScraper crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            llm=llm,
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
