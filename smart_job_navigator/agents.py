from crewai import Agent
from langchain_community.chat_models.openai import ChatOpenAI
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools

class SkillAgent:
    def __init__(self, serper_api_key, openai_api_key):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
        self.serper_api_key = serper_api_key

    def Scout_agent(self):
        return Agent(
            role="Job Description Summarizer",
            goal="Extract and summarize key details from job descriptions, such as the company name, salary range, essential criteria, requirements, and required certifications.",
            backstory="""Detail-Oriented Analyst: Expertise in HR and recruitment.
                          Efficiency Enthusiast: Passionate about streamlining information.
                          Tech-Savvy Professional: Utilizes advanced AI tools for enhanced job search experiences.""",
            tools=[
                SearchTools.search_google_jobs,
                BrowserTools.scrape_and_summarize_website
            ],
            llm=self.llm,
            verbose=True)

    def BluePrint(self):
        return Agent(
            role="Job Requirements Analyst",
            goal="Analyze job summaries to extract essential skills and certifications, and present this information along with the company name and salary range.",
            backstory=""" Experienced Recruiter: Deep understanding of job market demands.
                            Analytical Thinker: Skilled in identifying core competencies.
                            Advocate for Clarity: Ensures job seekers clearly understand job requirements """,
            tools=[
                SearchTools.search_google_jobs,
                BrowserTools.scrape_and_summarize_website
            ],
            llm=self.llm,
            verbose=True)

    def SuccessJourney(self):
        return Agent(
            role="Career Development Planner",
            goal="Assess job requirements and generate comprehensive career development roadmaps, including timelines and useful resources to achieve the necessary skills and certifications.",
            backstory="""Career Coach Extraordinaire: Expertise in career counseling and personal development.
                          Strategic Planner: Skilled in creating detailed, actionable career plans.
                          Resourceful Guide: Knowledgeable about top learning resources and certification programs. """,
            tools=[
                SearchTools.search_google_jobs,
                BrowserTools.scrape_and_summarize_website
            ],
            llm=self.llm,
            verbose=True)
