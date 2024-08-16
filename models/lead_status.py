from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from beanie import Document

class LeadStatus(Document):
    leadStatus:str
    status: str = "ACTIVE"
    displayIndex:str
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "leadstatuses"

    class Config:
        json_schema_extra = {
            "example": {
                "leadStatus": "NEW",
                "displayIndex": "1",
                "status": "ACTIVE"
            }
        }