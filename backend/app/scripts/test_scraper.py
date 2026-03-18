from app.services.job_ingestion_service import save_jobs_to_csv

if __name__ == "__main__":
    save_jobs_to_csv("jobs.csv")
    print("Jobs saved to jobs.csv")