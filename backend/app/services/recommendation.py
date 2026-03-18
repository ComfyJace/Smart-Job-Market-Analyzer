from collections import Counter
import pandas as pd
from app.skill_dictionary import SKILL_ALIASES
from app.services.analytics import extract_skills_from_text

def normalize_user_skills(user_skills: list[str]) -> list[str]:
    """
    Normalize user-provided skills into canonical skill names.

    Example:
    - 'js' -> 'javascript'
    - 'tf' -> 'tensorflow'
    """
    normalized = []

    for user_skill in user_skills:
        skill_lower = user_skill.lower().strip()
        matched = False

        for canonical_skill, aliases in SKILL_ALIASES.items():
            if skill_lower == canonical_skill or skill_lower in aliases:
                normalized.append(canonical_skill)
                matched = True
                break

        if not matched:
            normalized.append(skill_lower)

    return normalized

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

def analyze_role_skill_gap(role: str, user_skills: list[str], csv_path: str):
    """
    Analyze the gap between user skills and the skills required
    for a specific target job role.
    """
    df = pd.read_csv(csv_path)

    # Filter job posts whose title matches the target role
    filtered_df = df[df["title"].str.contains(role, case=False, na=False)]

    if filtered_df.empty:
        return {
            "role": role,
            "job_count": 0,
            "matched_skills": [],
            "missing_skills": [],
            "top_recommended": [],
            "message": f"No job listings found for role: {role}"
        }

    all_skills = []

    # Extract skills only from the filtered role
    for desc in filtered_df["description"]:
        skills = extract_skills_from_text(str(desc))
        all_skills.extend(skills)

    skill_counts = Counter(all_skills)

    # Normalize user skills for comparison
    normalized_user_skills = normalize_user_skills(user_skills)

    matched = []
    missing = []

    for skill in skill_counts.keys():
        if skill in normalized_user_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    missing_sorted = sorted(
        missing,
        key=lambda skill: skill_counts[skill],
        reverse=True
    )

    return {
        "role": role,
        "job_count": len(filtered_df),
        "matched_skills": matched,
        "missing_skills": missing_sorted,
        "top_recommended": missing_sorted[:3]
    }