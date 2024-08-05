# models.py
from typing import List
from beanie import Document
from pydantic import BaseModel, EmailStr
from datetime import datetime
from bson import ObjectId

class Staffs(Document):
    name: str
    gender: str
    emailId: EmailStr
    fatherName: str
    roleName: str
    mobileNumber: str
    alternateNumber:str
    dateOfJoining:str
    status:str
    roleName:str
    currentAddress:str
    permanentAddress:str
    ug:str
    # profileImage:str
    emergencyContactName1:str
    emergencyMobileNumber1:str
    emergencyRelationShip1:str
    emergencyContactName2:str
    emergencyMobileNumber2:str
    emergencyRelationShip2:str
    
    class Settings:
        name = "staffs"


