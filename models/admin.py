from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr,Field
from datetime import datetime

class Admin(Document):
    name: str
    email: EmailStr
    mobileNumber: str
    role:str
    status:str
    password:str
    createdDate: datetime = Field(default_factory=datetime.utcnow)
    updatedDate: datetime = Field(default_factory=datetime.utcnow)
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Asif",
                "email": "asif@shenll.dev",
                "password":"Admin@123",
                "mobileNumber":"9874563210",
                "role":"Python Dev",
                "status":"Active"
            }
        }

    class Settings:
        name = "admins"


class AdminSignIn(HTTPBasicCredentials):
    class Config:
        json_schema_extra = {
            "example": {"username": "anbarasan@shenll.com", "password": "admin@123"}
        }


class AdminData(BaseModel):
    name: str
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "name": "anbarasan",
                "email": "anbarasan@shenll.com",
            }
        }
