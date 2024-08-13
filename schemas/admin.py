from pydantic import BaseModel
from pydantic import EmailStr,Field
from datetime import datetime
from typing import Optional

class AdminSignIn(BaseModel):
    password: str
    email: EmailStr
    class Config:
        json_schema_extra = {
            "example": {"email": "abdul@youngest.dev", "password": "3xt3m#"}
        }


class AdminData(BaseModel):
    firstName: str
    lastName:str
    email: EmailStr
    phoneNumber: str
    password:str
    role: Optional[str] = "ADMIN"  # Default value for role
    status: Optional[str] = "ACTIVE"  # Default value for status
    createdDate: datetime = Field(default_factory=datetime)
    updatedDate: datetime = Field(default_factory=datetime)
    
    class Config:
        json_schema_extra = {
            "example": {
                "firstName": "siva",
                "lastName":"sankar",
                "email": "siva@shenll.dev",
                "phoneNumber":"8754740313",
                "password":"password"
            }
        }
        

class OTPResponse(BaseModel):
    status: str
    message: str
    data: dict
    
class AdminOTPVerification (BaseModel):
    email: EmailStr
    code: int


class ForgotPassword(BaseModel):
    email:EmailStr
    type:str

class ResetPassword(BaseModel):
    code: str
    password: str
    email: EmailStr