from crewai import Task
from textwrap import dedent
from datetime import date


class Tasks:
    def identify_jobs(self, agent, job_title, salary_range):
        return Task(
            description=dedent(
                f"""
                Identify and select the highest paying job based on the title "{job_title}".
                This task involves comparing salary ranges across various job descriptions
                to determine the best financial opportunity.

                Criteria:
                - Job Title: {job_title}
                - Desired Salary Range: {salary_range}

                Your final output should be a list of the top three highest paying jobs,
                including company names and their respective salary ranges.
            """
            ),
            expected_output="A list of the top three highest paying jobs, including company names and their respective salary ranges.",
            agent=agent,
        )

    def criterium_extracter(self, agent, job_title, salary_range):
        return Task(
            description=dedent(
                f"""
                Extract essential criteria from the job description for the title "{job_title}".
                This task involves scanning job descriptions and requirements for key
                skills, qualifications, and certifications.

                Criteria:
                - Job Title: {job_title}
                - Desired Salary Range: {salary_range}

                Your final output should be a summary of the essential criteria for the top three jobs,
                including required skills, qualifications, and certifications.
            """
            ),
            expected_output="A summary of the essential criteria for the top three jobs, including required skills, qualifications, and certifications.",
            agent=agent,
        )

    def skill_ranker(self, agent, job_title, salary_range):
        return Task(
            description=dedent(
                f"""
                Rank the required skills and certifications for the job title "{job_title}".
                This task involves listing and ranking jobs from highest to lowest paid based
                on the salary range provided.

                Criteria:
                - Job Title: {job_title}
                - Desired Salary Range: {salary_range}

                Your final output should be a ranked list of jobs with their required skills
                and certifications, from the highest paying to the lowest paying.
            """
            ),
            expected_output="A ranked list of jobs with their required skills and certifications, from the highest paying to the lowest paying.",
            agent=agent,
        )

    def road_map(self, agent, job_title, salary_range):
        return Task(
            description=dedent(
                f"""
                Create a personalized roadmap to become eligible for the highest paid job
                with the title "{job_title}". This task involves developing a step-by-step
                plan, including timelines and resources, to acquire the necessary skills
                and certifications.

                Criteria:
                - Job Title: {job_title}
                - Desired Salary Range: {salary_range}

                Your final output should be a detailed career development roadmap, including
                timelines and useful resources such as courses, books, and certification programs.
            """
            ),
            expected_output="A detailed career development roadmap, including timelines and useful resources such as courses, books, and certification programs.",
            agent=agent,
        )
