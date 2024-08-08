from beanie import Document
# from fastapi.security import HTTPBasicCredentials
from pydantic import Field
from datetime import datetime
from typing import Optional

class Organizations(Document):
    jobTitle:str
    status: str = "ACTIVE"
    createdAt:datetime = Field(default_factory=datetime.now)
    updatedAt:datetime = Field(default_factory=datetime.now)

    class Config:
        json_schema_extra = {
            "example": {
                "jobTitle": "developer",
            }
        }
    class Settings:
        name = "organizations"
