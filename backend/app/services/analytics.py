import pandas as pd
from collections import Counter
from app.skill_dictionary import SKILL_ALIASES

def extract_skills_from_text(text: str):
    """
    Extract normalized skills from raw job description text.

    Example:
    - 'js' becomes 'javascript'
    - 'ml' becomes 'machine learning'
    - 'tf' becomes 'tensorflow'
    """
    text = text.lower()
    found = set()

    for canonical_skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            if alias in text:
                found.add(canonical_skill)
                break

    return list(found)


def get_top_skills(csv_path: str):
    df = pd.read_csv(csv_path)

    all_skills = []

    for desc in df["description"]:
        skills = extract_skills_from_text(str(desc))
        all_skills.extend(skills)

    counter = Counter(all_skills)

    return dict(counter.most_common())

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