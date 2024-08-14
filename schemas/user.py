from pydantic import BaseModel, EmailStr
from typing import Optional, Any

class Response(BaseModel):
    status_code: int
    status:str
    message: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "status":"ok",
                "message": "Operation successful",
                "data": "Sample data",
            }
        }

class UpdateUserModel(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    # role: str
    # emailVerified: bool
    # mobileVerified: bool
    # subscribed: bool
    # subscriptionType: bool
    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "firstName":"firstname",
                "lastName":"lastname",
                "email":"email",
                "password":"password"
            }
        }