from pydantic import BaseModel,EmailStr

from datetime import datetime

class AdminSignIn(BaseModel):
    password: str
    email: EmailStr
    class Config:
        json_schema_extra = {
            "example": {"email": "abdul@youngest.dev", "password": "3xt3m#"}
        }


class AdminData(BaseModel):
    name: str
    email: EmailStr
    mobileNumber: str
    role: str
    status: str
    createdDate: datetime
    updatedDate: datetime
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Asif",
                "email": "asif@shenll.dev",
                "mobileNumber":"9874563210",
                "role":"Python Dev",
                "status":"Active"
            }
        }
        

class OTPResponse(BaseModel):
    status: str
    message: str
    data: dict
    
class AdminOTPVerification (BaseModel):
    email: EmailStr
    code: int