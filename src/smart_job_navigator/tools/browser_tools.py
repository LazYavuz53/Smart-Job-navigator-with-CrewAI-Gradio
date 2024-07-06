import os
import json
import requests
from bs4 import BeautifulSoup
from crewai import Agent, Task
from langchain.tools import tool
from crewai_tools import tool
from pyppeteer import launch

class BrowserTools:

    @tool("Scrape and summarize website content")
    async def scrape_and_summarize_website(self, website):
        """Useful to scrape and summarize a website content"""
        browser = await launch()
        page = await browser.newPage()
        await page.goto(website)
        content = await page.content()
        await browser.close()

        elements = BeautifulSoup(content, 'html.parser')
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
            summary = await task.execute()  # Ensure this is awaited
            summaries.append(summary)
        return "\n\n".join(summaries)
