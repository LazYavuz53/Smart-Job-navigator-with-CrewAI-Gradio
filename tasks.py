from crewai import Task
from textwrap import dedent
from datetime import date

class Tasks():

  def identify_jobs(self, agent, job_title, salary_range):
    return Task(description=dedent(f"""
        Analyze and select the highest paying job. This task involves comparing
        salary ranges in jobs description. 

        The job you are looking for: {job_title}
        The salary you are looking for: {salary_range}
      """),
                agent=agent)

  def criterium_extracter(self, agent, job_title, salary_range):
    return Task(description=dedent(f"""
        Extract the criterium from the job description. This task involves
        scanning the job description for keywords and phrases.

        The job you are looking for: {job_title}
        The salary you are looking for: {salary_range}
      """),
                agent=agent)

  def skill_ranker(self, agent, job_title, salary__range):
    return Task(description=dedent(f"""
        List the skills required for the job.
        This task involves ranking jobs from highest paid to lowest paid jobs

        The job you are looking for: {job_title}
        The salary you are looking for: {salary__range}
      """),
                agent=agent)
  
  def road_map(self, agent, job_title, salary__range):
    return Task(description=dedent(f"""
        Create a personilized road map to get eligible for the highest paid job.
        This task involves creating a road map for the job.

        The job you are looking for: {job_title}
        The salary you are looking for: {salary__range}
      """),
                agent=agent)
