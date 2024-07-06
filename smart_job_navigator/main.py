from fastapi import FastAPI
from pydantic import BaseModel

class JobDetails(BaseModel):
    job_title: str
    salary_range: str

from .crew import SkillCrew

app = FastAPI()

@app.post("/kickoff")
def kickoff_endpoint(job_details: JobDetails):
    crew = SkillCrew(job_details.job_title, job_details.salary_range)
    result = crew.run()
    return {"result": result}

@app.get("/")
def read_root():
    return {"message": "Welcome to the SkillCrew API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
