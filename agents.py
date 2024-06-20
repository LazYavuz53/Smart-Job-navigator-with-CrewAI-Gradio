from crewai import Agent
from langchain.llms import OpenAI

from tools.browser_tools import BrowserTool
from tools.search_tools import SearchTool

class SkillAgent():
    
    def Scout_agent(self):
        return Agent(
            role: "Job Description Summarizer",
            goal: "Extract and summarize key details from job descriptions, such as the company name, salary range, essential criteria, requirements, and required certifications.",
            backstory= """Detail-Oriented Analyst: Expertise in HR and recruitment.
                          Efficiency Enthusiast: Passionate about streamlining information.
                          Tech-Savvy Professional: Utilizes advanced AI tools for enhanced job search experiences.""",
            tools: [
                SearchTools.searh_internet,
                BrowserTools.scrape_and_summarize_website
            ],
            verbose: True)
    def BluePrint(self):
        return Agent(
            role: "Job Requirements Analyst",
            goal: "Analyze job summaries to extract essential skills and certifications, and present this information along with the company name and salary range.",
            backstory= """ Experienced Recruiter: Deep understanding of job market demands.
                            Analytical Thinker: Skilled in identifying core competencies.
                            Advocate for Clarity: Ensures job seekers clearly understand job requirements """,
            tools: [
                SearchTools.searh_internet,
                BrowserTools.scrape_and_summarize_website
            ],
            verbose: True)
    
    #def SkillSage(self):
        #return Agent(
         #   role: "Skill assessor",
          #  goal: "Assess the essential skills required by highest paid jobs",
           # backstory= "I am a skill assesor expert who is extracting essential skills
            #  "required by the highest paid jobs",
            #tools: [
             #   SearchTools.searh_internet,
              #  BrowserTools.scrape_and_summarize_website
            #],
            #verbose: True)
    def SuccessJourney(self):
        return Agent(
            role: "Career Development Planner",
            goal: "Assess job requirements and generate comprehensive career development roadmaps, including timelines and useful resources to achieve the necessary skills and certifications.",
            backstory= """Career Coach Extraordinaire: Expertise in career counseling and personal development.
                            Strategic Planner: Skilled in creating detailed, actionable career plans.
                            Resourceful Guide: Knowledgeable about top learning resources and certification programs. """,
            tools: [
                SearchTools.searh_internet,
                BrowserTools.scrape_and_summarize_website
            ],
            verbose: True)
    