from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from beanie import Document

class Jobtitles(Document):
    jobTitle:str
    status: str = "ACTIVE"
    createdAt:datetime = Field(default_factory=datetime.now)
    updatedAt:datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "jobtitles"

    class Config:
        json_schema_extra = {
            "example": {
                "jobTitle": "PYTHON DEVELOPER"
            }
        }