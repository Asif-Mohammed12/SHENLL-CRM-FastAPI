from datetime import datetime
from beanie import Document
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class OTP(Document):
    email: EmailStr
    code: int
    type: str  # e.g., "LOGIN"
    status: str = "INACTIVE"  # Can be "ACTIVE" or "INACTIVE"
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "asif@gmail.com",
                "code": 1234,
                "type": "LOGIN",
                "status": "INACTIVE",
                "createdAt": "2024-03-26T12:27:38.182Z",
                "updatedAt": "2024-03-26T12:27:38.182Z"
            }
        }

    class Settings:
        name = "otps"
