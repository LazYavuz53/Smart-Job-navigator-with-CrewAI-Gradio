import json
import os
import requests
from bs4 import BeautifulSoup
from crewai import Agent, Task
from langchain.tools import tool

class BrowserTools:

    @tool("Scrape and summarize website content")
    def scrape_and_summarize_website(website):
        """Useful to scrape and summarize a website content"""
        url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
        payload = json.dumps({"url": website})
        headers = {'Cache-Control': 'no-cache', 'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        elements = BeautifulSoup(response.text, 'html.parser')
        job_description = elements.get_text(separator='\n').strip()

        content_chunks = [job_description[i:i + 8000] for i in range(0, len(job_description), 8000)]
        summaries = []
        for chunk in content_chunks:
            agent = Agent(
                role='Principal Researcher',
                goal='Conduct detailed research and provide comprehensive summaries based on the content.',
                backstory="You're a Principal Researcher tasked with analyzing job listings to provide concise and relevant summaries.",
                allow_delegation=False)
            task = Task(
                agent=agent,
                description=f'Analyze and summarize the content below, including the most relevant information. Return only the summary.\n\nCONTENT\n----------\n{chunk}'
            )
            summary = task.execute()
            summaries.append(summary)
        return "\n\n".join(summaries)
