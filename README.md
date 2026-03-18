# Smart Job Market Analyzer

An AI-powered job market analytics platform that analyzes job listings to identify in-demand skills, trends, and personalized skill gaps for aspiring AI/ML engineers and data professionals.

---

## 🚀 Overview

The Smart Job Market Analyzer is designed to help users understand:

- What skills are most in demand in AI/ML roles
- How job requirements vary by role and location
- What skills they are missing based on real job market data
- What to learn next to stay competitive

This project combines **data science, backend engineering, and NLP** to deliver actionable insights from job listings.

---

## 🧠 Features

### ✅ Current Features
- FastAPI backend with REST API
- Job data ingestion from CSV
- Skill extraction from job descriptions
- Top skills analytics endpoint
- Clean project structure with virtual environment
- Git-managed repository with proper `.gitignore`

### 🔜 Planned Features
- Skill gap analysis (compare user skills vs market demand)
- Role-based skill comparison (ML Engineer vs Data Scientist)
- Interactive frontend dashboard (React)
- NLP-based skill extraction using spaCy
- Job trend analysis over time
- Recommendation engine for learning paths
- Unit and API testing with pytest
- Dockerized deployment

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- Pandas
- SQLAlchemy
- Pydantic

### Data Science / ML
- scikit-learn
- spaCy (planned)

### Frontend (planned)
- React (Vite)
- Chart.js / Recharts

### Tools
- Git & GitHub
- VS Code
- Virtual Environment (venv)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/smart-job-market-analyzer.git
cd smart-job-market-analyzer/backend

### 2. Create virtual environment
python -m venv venv

### 3. Activate virtual environment
```Windows```
venv\Scripts\activate
```Mac/Linux```
source venv/bin/activate
### 4. Install dependencies
pip install -r requirements.txt

### 5. Run the Server
uvicorn app.main:app --reload
