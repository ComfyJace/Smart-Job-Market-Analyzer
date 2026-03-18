import requests
from typing import List, Dict
from app.scrapers.base import BaseJobScraper


class GreenhouseScraper(BaseJobScraper):
    def __init__(self, board_token: str):
        self.board_token = board_token
        self.base_url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs?content=true"

    def fetch_jobs(self) -> List[Dict]:
        response = requests.get(self.base_url, timeout=30)
        response.raise_for_status()

        data = response.json()
        jobs = data.get("jobs", [])

        normalized_jobs = []

        for job in jobs:
            location = ""
            if isinstance(job.get("location"), dict):
                location = job["location"].get("name", "")

            normalized_jobs.append({
                "title": job.get("title", ""),
                "company": self.board_token,
                "location": location,
                "description": job.get("content", "") or "",
                "posted_date": None,
                "source": f"greenhouse:{self.board_token}",
                "source_type": "greenhouse",
                "url": job.get("absolute_url", ""),
            })

        return normalized_jobs