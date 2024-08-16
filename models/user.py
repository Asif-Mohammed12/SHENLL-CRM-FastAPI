# models.py
from typing import List
from beanie import Document
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from bson import ObjectId

class User(Document):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    role: str
    emailVerified: bool
    mobileVerified: bool
    subscribed: bool
    subscriptionType: bool
    createdAt:datetime = Field(default_factory=datetime.now)
    updatedAt:datetime = Field(default_factory=datetime.now)
    class Settings:
        name = "users"

# __all__ = [User]  # Include all your model classes here
