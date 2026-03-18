import pandas as pd
from collections import Counter
from app.skill_dictionary import SKILLS

def extract_skills_from_text(text: str):
    text = text.lower()
    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return found


def get_top_skills(csv_path: str):
    df = pd.read_csv(csv_path)

    all_skills = []

    for desc in df["description"]:
        skills = extract_skills_from_text(str(desc))
        all_skills.extend(skills)

    counter = Counter(all_skills)

    return dict(counter.most_common())