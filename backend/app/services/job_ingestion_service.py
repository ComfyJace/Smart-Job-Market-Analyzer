import pandas as pd
from app.scrapers.runner import run_all_scrapers

def save_jobs_to_csv(output_path: str):
    jobs = run_all_scrapers()

    if not jobs:
        raise ValueError("No jobs were fetched. CSV was not created.")

    df = pd.DataFrame(jobs)
    df.to_csv(output_path, index=False)
    print(f"Jobs saved to {output_path}")