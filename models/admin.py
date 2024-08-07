from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr,Field
from datetime import datetime

class Admin(Document):
    firstName: str
    lastName:str
    email: EmailStr
    phoneNumber: str
    role: str = "ADMIN"  # Default value for role
    status: str = "ACTIVE"  # Default value for status
    password:str
    createdDate: datetime = Field(default_factory=datetime.utcnow)
    updatedDate: datetime = Field(default_factory=datetime.utcnow)
    class Config:
        json_schema_extra = {
            "example": {
                "firstName": "siva",
                "lastName":"sankar",
                "email": "siva@shenll.dev",
                "phoneNumber":"8754740313",
                "password":"password"
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
