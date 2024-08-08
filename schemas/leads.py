from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import Optional, Any
from datetime import datetime

class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }


class LeadsCreate(BaseModel):
    namePrefix: Optional[str] = None
    firstName: str
    lastName: str
    jobTitle: Optional[str] = None
    organization: Optional[str] = None
    department: Optional[str] = None
    socialMediaUrl: Optional[str] = None
    employee: Optional[str] = None
    website: Optional[HttpUrl] = None
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
    countryCodeOffice: Optional[str] = None
    countryCodeMobile: Optional[str] = None
    leadSource: Optional[str] = None
    leadSourceAndDescription: Optional[str] = None
    industry: Optional[str] = None
    referredBy: Optional[str] = None
    leadStatus: Optional[str] = None
    statusDescription: Optional[str] = None
    campaign: Optional[str] = None
    opportunityAmount: Optional[str] = None
    assignedBy: Optional[str] = None
    profileImage: Optional[str] = None
    organizationLogo: Optional[str] = None
    status: Optional[str] = "ACTIVE"
    createdAt:  datetime = Field(default_factory=datetime)
    updatedAt:  datetime = Field(default_factory=datetime)
# class GetLeads(BaseModel):
#     namePrefix:str
#     firstName:str
#     lastName:str
#     jobTitle:str
#     organization:str
#     department:str
#     socialMediaUrl:str
#     employee:str
#     website:str
#     email:EmailStr
#     alternateEmail:EmailStr
#     officePhone:str
#     mobileNumber:str
#     address1:str
#     city1:str
#     postalCode1:str
#     state1:str
#     country1:str
#     address2:str
#     city2:str
#     postalCode2:str
#     state2:str
#     country2:str
#     countryCodeOffice:str
#     countryCodeMobile:str
#     leadSource:str
#     leadSourceAndDescription:str
#     industry:str
#     referredBy:str
#     leadStatus:str
#     statusDescription:str
#     campaign:str
#     opportunityAmount:str
#     assignedBy:str
#     profileImage:str
#     organizationLogo:str
#     status:str = "ACTIVE"
#     createdAt: datetime = Field(default_factory=datetime.utcnow)
#     updatedAt: datetime = Field(default_factory=datetime.utcnow)

    # class Config:
    #     json_schema_extra = {
    #         "example": {
    #             "status_code": 200,
    #             "response_type": "success",
    #             "description": "Operation successful",
    #             "data": "Sample data",
    #         }
        # }

        #     leads.firstName,
        # leads.department,
        # leads.organization,
        # leads.website,
        # leads.email,
        # leads.mobileNumber,
        # leads.status,