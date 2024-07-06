
## Project Overview

### Introduction

The Smart Job Navigator is an innovative, AI-driven application designed to streamline the job search and career planning process. Leveraging the powerful capabilities of CrewAI, FastAPI, and advanced language models, this application provides users with detailed career development roadmaps tailored to their desired job titles and salary ranges.

### Objectives

- **Automate Job Search**: Automatically extract and summarize key details from job descriptions.
- **Analyze Job Requirements**: Identify essential skills and certifications required for specific job roles.
- **Create Career Roadmaps**: Generate comprehensive career development plans, including timelines and recommended resources for skill acquisition and certification.

### Key Features

1. **Job Description Summarizer (Scout Agent)**
   - Extracts and summarizes key details from job descriptions, such as company names, salary ranges, essential criteria, requirements, and required certifications.

2. **Job Requirements Analyst (BluePrint Agent)**
   - Analyzes job summaries to extract essential skills and certifications, presenting this information along with the company name and salary range.

3. **Career Development Planner (SuccessJourney Agent)**
   - Assesses job requirements and generates detailed career development roadmaps, including timelines and useful resources to achieve the necessary skills and certifications.

### Project Structure

```sh
Smart Job Navigator/
├── README.md
├── pyproject.toml
├── requirements.txt
├── .env
├── smart_job_navigator/
│   ├── config/
│   │   ├── agents.yaml
│   │   └── tasks.yaml
│   ├── crew.py
│   ├── main.py
│   ├── agents.py
│   ├── tasks.py
│   └── tools/
│       └── browser_tools.py
        └── search_tools.py
```

### Technology Stack

- **Python**: Core programming language for development.
- **FastAPI**: Web framework for building the API.
- **CrewAI**: Framework for orchestrating autonomous AI agents.
- **LangChain**: Language model management and interaction.
- **dotenv**: For managing environment variables.
- **Uvicorn**: ASGI server for running FastAPI applications.

### How It Works

1. **User Input**: The user provides a job title and salary range through the web interface.
2. **Agent Orchestration**:
   - The **Scout Agent** identifies and summarizes job opportunities.
   - The **BluePrint Agent** analyzes job descriptions to extract requirements and essential skills.
   - The **SuccessJourney Agent** generates a tailored career development roadmap.
3. **Output**: The application returns a comprehensive career plan, helping the user navigate their career path with clarity and confidence.

### Setting Up the Project

1. **Clone the Repository**:

   ```sh
   git clone <repository-url>
   cd Smart-Job-Navigator
   ```

2. **Install Dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   - Create a .env file with the necessary environment variables such as API keys.

4. **Run the Application**:

   ``` sh
   uvicorn src.smart_job_navigator.main:app --reload
   ```

### Usage

- **API Endpoint**: The primary endpoint is /kickoff, which initiates the job search and career planning process.
- **Interactive Documentation**: Access the Swagger UI at http://127.0.0.1:8000/docs to interact with the API and explore its capabilities.

### Future Enhancements

- **User Authentication**: Secure the application with user login and personalized job tracking.
- **Enhanced Analytics**: Integrate advanced analytics to provide deeper insights into job trends and career progression.
- **Mobile Support**: Develop a mobile application to make the Smart Job Navigator accessible on the go.

### Conclusion

The Smart Job Navigator aims to revolutionize the job search and career planning landscape by providing personalized, AI-driven insights and roadmaps. With a strong foundation in CrewAI and FastAPI, it offers a robust, scalable solution to help individuals achieve their career goals.
