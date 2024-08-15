from beanie import Document
from pydantic import Field, EmailStr, BaseModel
from datetime import datetime
from typing import Optional,Any

class Response(BaseModel):
    status_code: int
    status:str
    message: str
    data: Optional[Any]
    class Config:
        json_schema_extra = {
            "example": {
                "status_code":200,
                "status": "ok",
                "message": "Organization record(s) found",
                "data": "Sample data",
            }
        }

class UpdateReports(BaseModel):
    accountName:str
    mobileNumber:str
    email:EmailStr
    user:str
    leadSource:str
    status:str ="ACTIVE"
    createdAt:datetime = Field(default_factory=datetime.utcnow)
    updatedAt:datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "accountName": "neme",
                "mobileNumber": "",
                "email": "abdul@school.com",
                "user": "admin",
                "leadSource": "LSource"
            }
        }