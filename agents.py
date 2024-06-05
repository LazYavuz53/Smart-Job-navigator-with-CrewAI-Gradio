from crewai import Agent
from langchain.llms import OpenAI

from tools.browser_tools import BrowserTool
from tools.search_tools import SearchTool

class SkillAgent():
    def Scout_agent(self):
        return Agent(
            role: "Filtering jobs based on essential criteria",
            goal: "Select the highest paid jobs",
            backstory= "I am a job picking expert who is looking for the highest paid jobs",
            tools: [
                SearchTools.searh_internet,
                BrowserTools.scrape_and_summarize_website
            ],
            verbose: True)
    def BluePrint(self):
        return Agent(
            role: "Requirement analyst",
            goal: "Analyze the requirements and essential skills from job description",
            backstory= "I am a requirement analyst expert who is looking for the requirements and essential skills in the job description",
            tools: [
                SearchTools.searh_internet,
                BrowserTools.scrape_and_summarize_website
            ],
            verbose: True)
    
    def SkillSage(self):
        return Agent(
            role: "Skill assessor",
            goal: "Assess the essential skills required by highest paid jobs",
            backstory= "I am a skill assesor expert who is extracting essential skills
              "required by the highest paid jobs",
            tools: [
                SearchTools.searh_internet,
                BrowserTools.scrape_and_summarize_website
            ],
            verbose: True)
    def SuccessJourney(self):
        return Agent(
            role: "Roadmap creator expert",
            goal: "Creates detailed roadmaps career progression",
            backstory= " Creates detailed roadmaps for projects or career progression, ensuring clear,"
              "step-by-step guidance towards goals",
            tools: [
                SearchTools.searh_internet,
                BrowserTools.scrape_and_summarize_website
            ],
            verbose: True)
    