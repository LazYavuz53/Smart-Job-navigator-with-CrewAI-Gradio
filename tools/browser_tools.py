import json
import os
import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html

class BrowserTools:

    @tool("Scrape and summarize job listing")
    def scrape_and_summarize_job_listing(website):
        """Useful to scrape and summarize a job listing content from a given website"""
        url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
        payload = json.dumps({"url": website})
        headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        elements = partition_html(text=response.text)
        content = "\n\n".join([str(el) for el in elements])
        content_chunks = [content[i:i + 8000] for i in range(0, len(content), 8000)]
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
