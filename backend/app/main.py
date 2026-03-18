"""
Smart Job Market Analyzer - Backend API

This module defines the main FastAPI application and API routes.

Responsibilities:
- Serve analytics endpoints
- Connect request layer to business logic
- Load and manage external data sources (CSV for now)

Author: ComfyJace
"""
from fastapi import FastAPI
from pathlib import Path
from pydantic import BaseModel

# Import business logic function
from app.services.analytics import get_top_skills
from app.services.recommendation import analyze_skill_gap

# Initialize FastAPI application
app = FastAPI()


# ==============================
# 📁 FILE PATH CONFIGURATION
# ==============================

# __file__ → current file (main.py)
# .resolve() → gets absolute path
# .parent → goes up one folder level

# This sets BASE_DIR to:
# backend/app → parent → backend
BASE_DIR = Path(__file__).resolve().parent.parent

# Navigate to project root, then into data folder
# backend → parent → project root → data/sample_jobs.csv
CSV_PATH = BASE_DIR.parent / "data" / "sample_jobs.csv"

class SkillGapRequest(BaseModel):
    user_skills: list[str]

# ==============================
# 🌐 API ROUTES
# ==============================

@app.get("/")
def read_root():
    """
    Root endpoint to verify API is running.
    Useful for quick checks and uptime validation.
    """
    return {"message": "API is working"}


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    Used in production systems to monitor service status.
    """
    return {"status": "ok"}


@app.get("/analytics/top-skills")
def top_skills():
    """
    Returns the most frequently occurring skills from job listings.

    Process:
    1. Load job data from CSV
    2. Extract skills from job descriptions
    3. Count occurrences of each skill
    4. Return ranked results

    Returns:
        dict: { skill_name: frequency }
    """
    return get_top_skills(str(CSV_PATH))

@app.post("/recommendations/skill-gap")
def skill_gap(request: SkillGapRequest):
    """
    Analyzes the skill gap between user-provided skills and job market demand.

    Input:
        list of user skills

    Output:
        matched skills, missing skills, and top recommendations
    """
    result = analyze_skill_gap(request.user_skills, str(CSV_PATH))
    return result