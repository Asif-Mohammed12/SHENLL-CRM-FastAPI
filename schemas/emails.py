from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Any
from datetime import datetime


class Response(BaseModel):
    status_code: int
    status: str
    message: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "status": "ok",
                "message": "Department record(s) found",
                "data": [
                    {
                        "department": "Development",
                        "status": "ACTIVE"
                    }
                ]
            }
        }

class UpdateEmails(BaseModel):
    to:Optional[EmailStr]
    cc:Optional[EmailStr]
    bcc:Optional[EmailStr]
    subject:str
    useTemplate:str
    status:str ="ACTIVE"
    createdAt:datetime=Field(default_factory=datetime.now)
    updatedAt:datetime=Field(default_factory=datetime.now)

    class Config:
        json_schema_extra = {
            "example": {
                "to": "janani@gmail.com",
                "cc": "aravind@gmail.com",
                "bcc": "mano@gmail.com",
                "subject": "Get priority access",
                "useTemplate": "NewTemplate",
            }
        }