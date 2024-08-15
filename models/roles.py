from beanie import Document
from pydantic import Field, EmailStr
from datetime import datetime
from typing import Optional

class Roles(Document):
    roleName:str
    status:str ="ACTIVE"
    createdAt:datetime = Field(default_factory=datetime.utcnow)
    updatedAt:datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "roleName": "abdul",
            }
        }

    class Settings:
        name = "roles"