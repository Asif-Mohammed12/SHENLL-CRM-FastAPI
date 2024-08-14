from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from beanie import Document

class LeadSource(Document):
    leadSoure:str
    status:str = "ACTIVE"
    displayIndex:str
    createdAt:datetime = Field(default_factory=datetime.utcnow)
    updatedAt:datetime = Field(default_factory=datetime.utcnow)
    class Settings:
        name = "leadsources"

    class Config:
        json_schema_extra = {
            "example": {
                "leadSoure": "REFERRAL",
                "displayIndex": "1",
                "status": "ACTIVE"
            }
        }