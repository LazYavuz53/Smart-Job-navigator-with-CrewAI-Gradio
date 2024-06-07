from crewai import crew
from textwrap import dedent
from agents import SkillAgent
from tasks import Tasks
from dotenv import load_dotenv

load_dotenv()

class SkillCrew:

    def __init__(self, job_title, salary_range):
        self.skill_agent = skill_agent
        self.tasks = tasks

    def run(self):
        agents=SkillAgent()
        tasks=Tasks()

        job_filterer_agent = agents.Scout_agent()
        requirement_analysis = agents.BluePrint()
        skill_assessment = agents.SkillSage()
        creation_of_roadmap = agents.SuccessJourney()

        task_identification = tasks.identify_jobs(
            job_filterer_agent,
            self.job_title,
            self.salary_range
        )

        extraction_of_requirements = tasks.criterium_extracter(
            requirement_analysis,
            self.job_title,
            self.salary_range
        )

        ranking_of_skills = tasks.skill_ranker(
            skill_assessment,
            self.job_title,
            self.salary_range
        )

        roadmap_creation = tasks.roadmap_creator(
            creation_of_roadmap,
            self.job_title,
            self.salary_range
        )

        crew = Crew(
            agents = [
                job_filterer_agent,
                requirement_analysis,
                skill_assessment,
                creation_of_roadmap
            ]
            tasks = [
                task_identification,
                extraction_of_requirements,
                ranking_of_skills,
                roadmap_creation
            ],
            verbose = True
        )
        result = crew.kickoff()
        return result
    
    if __name__ == "__main__":
        
        print(## Welcome to the Skill Crew ##)
        print(## We are going to help you create a roadmap for your next job ##)
        print(## Please enter the job title and salary range ##)
        print(## Example: Data Scientist, $50,000 - $100,000 ##)

        job_title = input("Enter the job title: ")
        salary_range = input("Enter the salary range: ")

        crew = SkillCrew(job_title, salary_range)
        result = SkillCrew.run()

        print("\n\n########################")
        print("## Your roadmap is ready ##")
        print(result)
