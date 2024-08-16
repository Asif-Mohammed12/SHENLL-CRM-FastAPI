from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from beanie import Document

class Countries(Document):
    cca2:Optional[str] = None

    class Settings:
        name = "countries"

    class Config:
        json_schema_extra = {
            "example": {
                "cca2": "cy"
            }
        }