from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from bson import ObjectId
from beanie import Document
from pydantic import BaseModel
# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not isinstance(v, ObjectId):
#             raise TypeError('Invalid ObjectId')
#         return v
class Leads(Document):
    namePrefix: Optional[str]
    firstName: str
    lastName: str
    jobTitle: Optional[str]
    organization: Optional[str]
    department: Optional[str]
    socialMediaUrl: Optional[str]
    employee: Optional[str]
    email: EmailStr
    alternateEmail: Optional[EmailStr]
    officePhone: Optional[str]
    mobileNumber: Optional[str]
    address1: str
    city1: str
    postalCode1: str
    state1: str
    country1: str
    address2: Optional[str]
    city2: Optional[str]
    postalCode2: Optional[str]
    state2: Optional[str]
    country2: Optional[str]
    countryCodeOffice: Optional[str]
    countryCodeMobile: Optional[str]
    leadSourceAndDescription: Optional[str]
    industry: Optional[str]
    statusDescription: Optional[str]
    campaign: Optional[str]
    opportunityAmount: Optional[str]
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "leads"

    class Config:
        json_schema_extra = {
            "example": {
                "firstName": "Siva",
                "department": "Developer",
                "organization": "Shenll Technology",
                "email": "siva@shenll.dev",
                "mobileNumber": "9876543210",
                "statusDescription": "ACTIVE"
            }
        }