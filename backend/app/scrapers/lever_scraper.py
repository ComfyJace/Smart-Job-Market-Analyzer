import requests
from typing import List, Dict
from app.scrapers.base import BaseJobScraper


class LeverScraper(BaseJobScraper):
    def __init__(self, company_slug: str):
        self.company_slug = company_slug
        self.base_url = f"https://api.lever.co/v0/postings/{company_slug}?mode=json"

    def fetch_jobs(self) -> List[Dict]:
        response = requests.get(self.base_url, timeout=30)
        response.raise_for_status()

        jobs = response.json()
        normalized_jobs = []

        for job in jobs:
            categories = job.get("categories", {}) or {}
            location = categories.get("location", "")

            description_parts = [
                job.get("descriptionPlain", "") or "",
                job.get("lists", [{}])[0].get("text", "") if job.get("lists") else "",
            ]
            description = "\n".join(part for part in description_parts if part)

            normalized_jobs.append({
                "title": job.get("text", ""),
                "company": self.company_slug,
                "location": location,
                "description": description,
                "posted_date": None,
                "source": f"lever:{self.company_slug}",
                "source_type": "lever",
                "url": job.get("hostedUrl", ""),
            })

        return normalized_jobs