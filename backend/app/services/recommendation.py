from collections import Counter
import pandas as pd
from app.skill_dictionary import get_alias_map
from app.services.analytics import extract_skills_from_text

_ALIAS_MAP = get_alias_map(include_short_aliases=True)
def normalize_user_skills(user_skills: list[str]) -> list[str]:
    """
    Normalize user-provided skills into canonical skill names.

    Example:
    - 'js' -> 'javascript'
    - 'tf' -> 'tensorflow'
    """
    normalized = []

    for user_skill in user_skills:
        if not isinstance(user_skill, str):
            continue
        
        skill_lower = user_skill.lower().strip()
        canonical_skill = _ALIAS_MAP.get(skill_lower)
        normalized.append(canonical_skill if canonical_skill else skill_lower)
  
    return normalized

def analyze_skill_gap(user_skills: list, csv_path: str):
    df = pd.read_csv(csv_path)

    if "description" not in df.columns:
      raise ValueError("CSV must contain a 'description' column.")
    
    all_skills = []

    # Extract all skills from job descriptions
    for desc in df["description"]:
        skills = extract_skills_from_text(str(desc))
        all_skills.extend(skills)

    skill_counts = Counter(all_skills)

    # Normalize user input
    normalized_user_skills = set(normalize_user_skills(user_skills))

    matched = []
    missing = []

    for skill in skill_counts.keys():
        if skill in normalized_user_skills:
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
        "top_recommendations": missing_sorted[:3]
    }

def analyze_role_skill_gap(role: str, user_skills: list[str], csv_path: str):
    """
    Analyze the gap between user skills and the skills required
    for a specific target job role.
    """
    df = pd.read_csv(csv_path)

    if "title" not in df.columns or "description" not in df.columns:
        raise ValueError("CSV must contain 'title' and 'description' columns.")
    
    # Filter job posts whose title matches the target role
    filtered_df = df[df["title"].str.contains(role, case=False, na=False)]

    if filtered_df.empty:
        return {
            "matched_skills": [],
            "missing_skills": [],
            "top_recommendations": [],
        }

    all_skills = []

    # Extract skills only from the filtered role
    for desc in filtered_df["description"]:
        skills = extract_skills_from_text(str(desc))
        all_skills.extend(skills)

    skill_counts = Counter(all_skills)

    # Normalize user skills for comparison
    normalized_user_skills = set(normalize_user_skills(user_skills))

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
        "matched_skills": matched,
        "missing_skills": missing_sorted,
        "top_recommendations": missing_sorted[:3]
    }