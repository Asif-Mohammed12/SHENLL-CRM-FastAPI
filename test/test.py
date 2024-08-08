from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from bson import ObjectId
from beanie import Document

class Leads(Document):
    namePrefix: Optional[str]
    firstName: str
    lastName: str
async def test_connection():
    client = AsyncIOMotorClient("mongodb://localhost:27017/crm")
    # collection = client.Leads
    documents = await Leads.all().to_list(length=10)
    print(documents)

import asyncio
asyncio.run(test_connection())