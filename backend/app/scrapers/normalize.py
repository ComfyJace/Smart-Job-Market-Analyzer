from pydantic import BaseModel
from typing import Optional


class NormalizedJob(BaseModel):
    title: str
    company: str
    location: str
    description: str
    posted_date: Optional[str] = None
    source: str
    source_type: str
    url: str