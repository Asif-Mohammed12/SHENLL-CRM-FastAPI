from typing import List, Optional
from beanie import Document,PydanticObjectId
from pydantic import  EmailStr,Field
from datetime import datetime

class Staffs(Document):
    name: str
    gender: str
    emailId: EmailStr
    fatherName: str
    roleName: str
    mobileNumber: str
    alternateNumber: str
    dateOfJoining: datetime = Field(default_factory=datetime.utcnow)
    status: str
    roleName: str
    currentAddress: str
    permanentAddress: str
    ug: str
    profileImage: Optional[bytes] = None 
    selectStatus: Optional[str] = None 
    emergencyContactName1: str
    emergencyMobileNumber1: str
    emergencyRelationShip1: str
    emergencyContactName2: str
    emergencyMobileNumber2: str
    emergencyRelationShip2: str
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)
    reportTo: Optional[PydanticObjectId] = None

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "name": "Abdulazeez Abdulazeez Adeshina",
                "gender": "Male",
                "emailId": "abdul@school.com",
                "fatherName": "John Doe",
                "roleName": "Teacher",
                "mobileNumber": "1234567890",
                "alternateNumber": "0987654321",
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
                "createdAt": "2023-01-01T00:00:00",
                "updatedAt": "2023-01-02T00:00:00",
                "reportTo": "60d5ec49f9b1b143c4a0b3a3"
            }
        }

    class Settings:
        name = "staffs"
