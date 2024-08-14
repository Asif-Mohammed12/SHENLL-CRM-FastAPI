from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import Optional, Any
from datetime import datetime
from beanie import PydanticObjectId


class Response(BaseModel):
    status_code: int
    status:str
    message: str
    data: Optional[Any]
    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "status": "ok",
                "message": "Leads record(s) found",
                "data": "Sample data",
            }
        }


class UpdateLead(BaseModel):
    namePrefix: Optional[str] = None
    firstName: str
    lastName: str
    jobTitle: Optional[str] = None
    socialMediaUrl: Optional[str] = None
    employee: Optional[str] = None
    website: Optional[str] = None
    email: EmailStr
    alternateEmail: Optional[EmailStr] = None
    officePhone: Optional[str] = None
    mobileNumber: Optional[str] = None
    address1: str
    city1: str
    postalCode1: str
    state1: str
    country1: str
    address2: Optional[str] = None
    city2: Optional[str] = None
    postalCode2: Optional[str] = None
    state2: Optional[str] = None
    country2: Optional[str] = None
    leadSource: Optional[PydanticObjectId] = None
    leadStatus: Optional[PydanticObjectId] = None
    leadSourceAndDescription: Optional[str] = None
    statusDescription: Optional[str] = None
    campaign: Optional[str] = None
    countryCodeOffice: Optional[str] = None
    countryCodeMobile: Optional[str] = None
    opportunityAmount: Optional[str] = None
    referredBy: Optional[PydanticObjectId] = None
    assignedBy: Optional[PydanticObjectId] = None
    profileImage: Optional[str] = None
    organizationLogo: Optional[str] = None
    status: str = "ACTIVE"
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "leads"

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "status": "success",
                "message": "Staff data retrieved successfully",
                "data": {
                    "id": "66bc891c714ab06ff04bba94",
                    "name": "Abdulazeez Abdulazeez Adeshina",
                    "gender": "Male",
                    "emailId": "abdul@clg.com",
                    "fatherName": "John Doe",
                    "roleName": "Teacher",
                    "mobileNumber": "9876543212",
                    "alternateNumber": "0987654323",
                    "dateOfJoining": "2023-01-01",
                    "status": "Active",
                    "currentAddress": "123 Main St",
                    "permanentAddress": "456 Elm St",
                    "ug": "B.Sc",
                    "profileImage": "path/to/image.jpg",
                    "selectStatus": "Selected",
                    "emergencyContactName1": "Jane Doe",
                    "emergencyMobileNumber1": "1234567890",
                    "emergencyRelationShip1": "Spouse",
                    "emergencyContactName2": "Joe Doe",
                    "emergencyMobileNumber2": "0987654321",
                    "emergencyRelationShip2": "Brother",
                }
            }
        }



