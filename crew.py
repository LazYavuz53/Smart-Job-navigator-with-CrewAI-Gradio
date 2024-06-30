from crewai import Crew
from textwrap import dedent
from agents import SkillAgent
from tasks import Tasks
from dotenv import load_dotenv

load_dotenv()

class SkillCrew:
    def __init__(self, job_title, salary_range):
        self.job_title = job_title
        self.salary_range = salary_range
        self.skill_agent = SkillAgent()
        self.tasks = Tasks()

    def run(self):
        job_filterer_agent = self.skill_agent.Scout_agent()
        requirement_analysis = self.skill_agent.BluePrint()
        # skill_assessment = self.skill_agent.SkillSage()
        creation_of_roadmap = self.skill_agent.SuccessJourney()

        task_identification = self.tasks.identify_jobs(
            job_filterer_agent,
            self.job_title,
            self.salary_range
        )

        extraction_of_requirements = self.tasks.criterium_extracter(
            requirement_analysis,
            self.job_title,
            self.salary_range
        )

        # ranking_of_skills = self.tasks.skill_ranker(
            # skill_assessment,
            # self.job_title,
            # self.salary_range
        # )

        roadmap_creation = self.tasks.road_map(
            creation_of_roadmap,
            self.job_title,
            self.salary_range
        )

        crew = Crew(
            agents=[
                job_filterer_agent,
                requirement_analysis,
                # skill_assessment,
                creation_of_roadmap
            ],
            tasks=[
                task_identification,
                extraction_of_requirements,
                # ranking_of_skills,
                roadmap_creation
            ],
            verbose=True
        )
        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("## Welcome to the Skill Crew ##")
    print("## We are going to help you create a roadmap for your next job ##")
    print("## Please enter the job title and salary range ##")
    print("## Example: Data Scientist, $50,000 - $100,000 ##")

    job_title = input("Enter the job title: ")
    salary_range = input("Enter the salary range: ")

    # Use mock data or smaller tasks for testing to reduce API usage
    if job_title.lower() == "test":
        job_title = "Data Scientist"
        salary_range = "$50,000 - $100,000"

    crew = SkillCrew(job_title, salary_range)
    result = crew.run()

    print("\n\n########################")
    print("## Your roadmap is ready ##")
    print(result)
