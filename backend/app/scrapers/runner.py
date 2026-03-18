from app.scrapers.greenhouse_scraper import GreenhouseScraper
from app.scrapers.lever_scraper import LeverScraper

def run_all_scrapers():
    scrapers = [
        # Replace with a real Greenhouse or Lever target
        GreenhouseScraper("coinbase"),  # Example Greenhouse board token
        LeverScraper("coinbase"),  # Example Lever company slug
    ]

    all_jobs = []

    for scraper in scrapers:
        try:
            jobs = scraper.fetch_jobs()
            print(f"{scraper.__class__.__name__}: fetched {len(jobs)} jobs")
            all_jobs.extend(jobs)
        except Exception as e:
            print(f"Scraper failed: {scraper.__class__.__name__} -> {e}")

    print(f"Total jobs fetched: {len(all_jobs)}")
    return all_jobs