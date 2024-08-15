from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from beanie import Document

class Departments(Document):
    department:str
    status: str = "ACTIVE"
    createdAt:datetime = Field(default_factory=datetime.now)
    updatedAt:datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "departments"

    class Config:
        json_schema_extra = {
            "example": {
                "department": "Testing",
                "status": "ACTIVE"
            }
        }