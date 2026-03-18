import pandas as pd
import re
from collections import Counter
from app.skill_dictionary import SKILL_ALIASES

def count_skills_from_descriptions(descriptions):
    all_skills = []

    for desc in descriptions:
        skills = extract_skills_from_text(desc)
        all_skills.extend(skills)

    return dict(Counter(all_skills).most_common())

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
            pattern = r'\b' + re.escape(alias) + r'\b'
            if re.search(pattern, text):
                found.add(canonical_skill)
                break

    return list(found)


def get_top_skills(csv_path: str):
    df = pd.read_csv(csv_path)

    if "description" not in df.columns:
        raise ValueError("CSV must contain a 'description' column.")

    return count_skills_from_descriptions(df["description"])

def get_top_skills_by_role(role: str, csv_path: str):
    df = pd.read_csv(csv_path)

    # Filter rows whose title contains the requested role text
    filtered_df = df[df["title"].str.contains(role, case=False, na=False)]

    if "title" not in df.columns or "description" not in df.columns:
        raise ValueError("CSV must contain 'title' and 'description' columns.")
    
    if filtered_df.empty:
        return {
            "role": role,
            "job_count": 0,
            "top_skills": {}
        }

    return {
        "role": role,
        "job_count": len(filtered_df),
        "top_skills": count_skills_from_descriptions(filtered_df["description"])
    }

def compare_roles(role_a: str, role_b: str, csv_path: str):
  skills_a = get_top_skills_by_role(role_a, csv_path)
  skills_b = get_top_skills_by_role(role_b, csv_path)
  
  shared_skills = set(skills_a["top_skills"].keys()) & set(skills_b["top_skills"].keys())
  unique_a = set(skills_a["top_skills"].keys()) - shared_skills
  unique_b = set(skills_b["top_skills"].keys()) - shared_skills
  return {
      "role_a": skills_a,
      "role_b": skills_b,
      "shared_skills": list(shared_skills),
      "unique_to_role_a": list(unique_a),
      "unique_to_role_b": list(unique_b)
  }