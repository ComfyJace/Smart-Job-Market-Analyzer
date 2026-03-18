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
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path



# Import business logic function
from app.services.analytics import get_top_skills, get_top_skills_by_role, compare_roles
from app.services.recommendation import analyze_skill_gap, analyze_role_skill_gap
from app.schemas import SkillGapRequest, RoleSkillGapRequest, SkillGapResponse, RoleSkillsResponse

# Initialize FastAPI application
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.post("/recommendations/skill-gap", response_model=SkillGapResponse)
def skill_gap(request: SkillGapRequest):
    """
    Analyzes the skill gap between user-provided skills and job market demand.

    Input:
        list of user skills

    Output:
        matched skills, missing skills, and top recommendations
    """
    return analyze_skill_gap(request.user_skills, str(CSV_PATH))

@app.post("/analytics/role-skills", response_model=RoleSkillsResponse)
def role_skills(role: str):
    """
    Analyzes top skills for a specific job role.

    Input:
        role (string)

    Output:
        job count and ranked skill list for that role
    """
    # For demonstration, we hardcode a role. In production, this would be dynamic.
    return get_top_skills_by_role(role, str(CSV_PATH))

@app.post("/recommendations/role-skill-gap")
def role_skill_gap(request: RoleSkillGapRequest):
    """
    Analyzes the skill gap for a specific target job role.

    Input:
        role (string)
        user_skills (list of strings)
    Output:
        matched skills, missing skills, top recommendations, and job count for that role
    """
    return analyze_role_skill_gap(
        request.role,
        request.user_skills,
        str(CSV_PATH)
    )

@app.post("/analytics/compare-roles")
def compare_jobs(role_a: str, role_b: str):
    """
    Compares the top skills between two job roles.

    Input:
        role_a (string)
        role_b (string)

    Output:
        top skills for each role and their overlap
    """
    return compare_roles(role_a, role_b, str(CSV_PATH))