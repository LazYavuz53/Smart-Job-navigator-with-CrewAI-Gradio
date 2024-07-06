from fastapi import FastAPI
from src.smart_job_navigator.crew import SkillCrew

app = FastAPI()

@app.post("/kickoff")
def kickoff_endpoint(job_title: str, salary_range: str):
    crew = SkillCrew(job_title, salary_range)
    result = crew.run()
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
