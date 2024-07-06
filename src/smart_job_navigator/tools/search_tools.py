import json
import os
import requests
from langchain.tools import tool
from crewai_tools import tool

class SearchTools:

    @tool("Search Google for jobs")
    def search_google_jobs(query, location=""):
        """Useful to search Google for jobs based on a given query and location, returning relevant results"""
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({
            "q": f"{query} jobs in {location}",
            "gl": "us",  # Adjust the location code as necessary
            "hl": "en"   # Adjust the language code as necessary
        })
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=payload)
        results = response.json()

        if 'organic' not in results:
            return "Sorry, I couldn't find anything about that, there could be an error with your Serper API key."
        else:
            job_listings = results['organic']
            string = []
            for job in job_listings[:top_result_to_return]:  # Limiting to top 4 results
                try:
                    string.append('\n'.join([
                        f"Title: {job['title']}",
                        f"Company: {job['rich_snippet']['top']['detectedExtensions'].get('company', 'N/A')}",
                        f"Location: {job['rich_snippet']['top']['detectedExtensions'].get('location', 'N/A')}",
                        f"Description: {job['snippet']}",
                        f"Link: {job['link']}",
                        "\n-----------------"
                    ]))
                except KeyError:
                    continue

            return '\n'.join(string)
