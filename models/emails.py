from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from beanie import Document




class Emails(Document):
    to:Optional[EmailStr]
    cc:Optional[EmailStr]
    bcc:Optional[EmailStr]
    subject:str
    useTemplate:str
    status:str ="ACTIVE"
    createdAt:datetime=Field(default_factory=datetime.now)
    updatedAt:datetime=Field(default_factory=datetime.now)

    class Settings:
        name = "emails"

    class Config:
        json_schema_extra = {
            "example": {
                "to": "janani@gmail.com",
                "cc": "aravind@gmail.com",
                "bcc": "mano@gmail.com",
                "subject": "Get priority access",
                "useTemplate": "NewTemplate",
            }
        }
