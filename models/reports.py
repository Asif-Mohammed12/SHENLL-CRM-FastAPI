from beanie import Document
from pydantic import Field, EmailStr
from datetime import datetime
from typing import Optional

class Reports(Document):
    accountName:str
    mobileNumber:str
    email:EmailStr
    user:str
    leadSource:str
    status:str ="ACTIVE"
    createdAt:datetime = Field(default_factory=datetime.utcnow)
    updatedAt:datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "accountName": "neme",
                "mobileNumber": "",
                "email": "abdul@school.com",
                "user": "admin",
                "leadSource": "LSource"
            }
        }

    class Settings:
        name = "reports"

