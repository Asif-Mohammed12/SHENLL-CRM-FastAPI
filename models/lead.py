from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from bson import ObjectId
from beanie import Document,PydanticObjectId
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
    socialMediaUrl: Optional[str]
    employee: Optional[str]
    # website: Optional[str]
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
    # leadSource: Optional[PydanticObjectId]  # Assuming this is a reference ID
    # leadStatus: Optional[PydanticObjectId]  # Assuming this is a reference ID
    leadSourceAndDescription: Optional[str]
    statusDescription: Optional[str]
    campaign: Optional[str]  # Corrected from "campaogh"
    countryCodeOffice: Optional[str]
    countryCodeMobile: Optional[str]
    opportunityAmount: Optional[str]
    # referredBy: Optional[PydanticObjectId]  # Assuming this is a reference ID
    # assignedBy: Optional[PydanticObjectId]  # Assuming this is a reference ID
    # profileImage: Optional[str]
    # organizationLogo: Optional[str]
    status: Optional[str]  # Example: "ACTIVE", "INACTIVE", etc.
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "leads"

    class Config:
        json_schema_extra = {
             "example": {
                "firstName": "Siva",
                "lastName": "Ramesh",
                "jobTitle": "Doctor",
                "socialMediaUrl": "https://in.linkedin.com/",
                "employee": "14",
                "website": "www.smartweb.com",
                "email": "test@gmail.com",
                "alternateEmail": "deal222@gmail.com",
                "officePhone": "9834572345",
                "mobileNumber": "9834572355",
                "address1": "DreamVillaAppartment, KK Nagar, Chennai, Tamil Nadu 600058",
                "city1": "Chennai",
                "postalCode1": "600067",
                "state1": "Tamilnadu",
                "country1": "India",
                "address2": "Chennai Food Town, KK Nagar, Chennai, Tamil Nadu 600058",
                "city2": "Chennai",
                "postalCode2": "600034",
                "state2": "Tamilnadu",
                "country2": "India",
                "leadSource": "66042752a4d52da314096db5",
                "leadStatus": "6603eb73f5ce2d70ffc92811",
                "leadSourceAndDescription": "Sample Data",
                "statusDescription": "Test Data",
                "campaign": "AU23424",
                "countryCodeOffice": "US",
                "countryCodeMobile": "UK",
                "opportunityAmount": "234",
                "referredBy": "6602cf390b3d4e8049b94d85",
                "assignedBy": "65e0c7513ecb78c104f34ee7",
                "profileImage": "/profile/imageUrl_1711534088125_photo3.jpeg",
                "organizationLogo": "/organization/imageUrl_1711534088125_photo3.jpeg",
                "status": "ACTIVE"
            }
        }


