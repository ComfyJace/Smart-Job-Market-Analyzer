import pandas as pd
from collections import Counter
from app.services.analytics import extract_skills_from_text


def get_top_skills_by_role(role: str, csv_path: str):
    df = pd.read_csv(csv_path)

    # Filter rows whose title contains the requested role text
    filtered_df = df[df["title"].str.contains(role, case=False, na=False)]

    if filtered_df.empty:
        return {
            "role": role,
            "job_count": 0,
            "top_skills": {}
        }

    all_skills = []

    for desc in filtered_df["description"]:
        skills = extract_skills_from_text(str(desc))
        all_skills.extend(skills)

    skill_counts = Counter(all_skills)

    return {
        "role": role,
        "job_count": len(filtered_df),
        "top_skills": dict(skill_counts.most_common())
    }