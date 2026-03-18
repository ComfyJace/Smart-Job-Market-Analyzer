from pydantic import BaseModel, Field, RootModel

class SkillGapRequest(BaseModel):
    user_skills: list[str]
    model_config = {
        "json_schema_extra": {
            "example": {
                "user_skills": ["python", "sql"]
            }
        }
    }

class RoleSkillGapRequest(BaseModel):
    role: str
    user_skills: list[str]
    model_config = {
        "json_schema_extra": {
            "example": {
                "role": "Data Scientist",
                "user_skills": ["python", "sql"]
            }
        }
    }
class SkillGapResponse(BaseModel):
    matched_skills: list[str] = Field(description="Skills that match between user input and job market demand")
    missing_skills: list[str] = Field(description="Skills found in the market but missing from the user's profile")
    top_recommendations: list[str] = Field(description="Highest-priority missing skills to learn next")

class RoleSkillsResponse(BaseModel):
    role: str
    job_count: int
    top_skills: dict[str, int]
