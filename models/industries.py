from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from beanie import Document

class Industries(Document):
    industry:str
    status: str = "ACTIVE"
    createdAt:datetime = Field(default_factory=datetime.now)
    updatedAt:datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "industries"

    class Config:
        json_schema_extra = {
            "example": {
                "industry": "IT"
            }
        }