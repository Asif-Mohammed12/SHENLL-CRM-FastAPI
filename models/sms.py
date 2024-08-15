from beanie import Document
from pydantic import Field, EmailStr
from datetime import datetime
from typing import Optional

class Sms(Document):
    to:EmailStr
    headline:str
    useTemplate:str
    status:str ="ACTIVE"
    createdAt:datetime = Field(default_factory=datetime.utcnow)
    updatedAt:datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "to": "abdul@school.com",
                "headline": "datas",
                "useTemplate": "Template",
            }
        }

    class Settings:
        name = "sms"