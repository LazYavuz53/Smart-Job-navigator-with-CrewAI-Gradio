import json
import os
import requests
from langchain.tools import tool

class SearchTools:

    @tool("Search Indeed for jobs")
    def search_indeed_jobs(query, location=""):
        """Useful to search Indeed for jobs based on a given query and location, returning relevant results"""
        top_result_to_return = 4
        url = "https://api.indeed.com/ads/apisearch"
        payload = {
            "publisher": os.environ['INDEED_PUBLISHER_ID'],
            "q": query,
            "l": location,
            "sort": "date",
            "radius": "25",
            "st": "employer",
            "jt": "",
            "start": "0",
            "limit": top_result_to_return,
            "format": "json",
            "v": "2"
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(url, params=payload, headers=headers)
        results = response.json()
        if 'results' not in results:
            return "Sorry, I couldn't find anything about that, there could be an error with your Indeed API key."
        else:
            job_listings = results['results']
            string = []
            for job in job_listings:
                try:
                    string.append('\n'.join([
                        f"Job Title: {job['jobtitle']}",
                        f"Company: {job['company']}",
                        f"Location: {job['formattedLocation']}",
                        f"Snippet: {job['snippet']}",
                        f"Link: {job['url']}",
                        "\n-----------------"
                    ]))
                except KeyError:
                    continue

            return '\n'.join(string)
