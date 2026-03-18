from collections import Counter
import pandas as pd
from app.skill_dictionary import SKILLS
from app.services.analytics import extract_skills_from_text


def analyze_skill_gap(user_skills: list, csv_path: str):
    df = pd.read_csv(csv_path)

    all_skills = []

    # Extract all skills from job descriptions
    for desc in df["description"]:
        skills = extract_skills_from_text(str(desc))
        all_skills.extend(skills)

    skill_counts = Counter(all_skills)

    # Normalize user input
    user_skills = [s.lower() for s in user_skills]

    matched = []
    missing = []

    for skill in skill_counts.keys():
        if skill in user_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    # Rank missing skills by demand
    missing_sorted = sorted(
        missing,
        key=lambda x: skill_counts[x],
        reverse=True
    )

    return {
        "matched_skills": matched,
        "missing_skills": missing_sorted,
        "top_recommended": missing_sorted[:3]
    }