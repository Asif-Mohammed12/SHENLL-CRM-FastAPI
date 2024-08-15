from pydantic import BaseModel, EmailStr,Field
from typing import Optional, Any
import datetime


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

class UpdateSms(BaseModel):
    to:EmailStr
    headline:str
    useTemplate:str
    status:str ="ACTIVE"


    class Config:
        json_schema_extra = {
            "example": {
                "to": "abdul@school.com",
                "headline": "datas",
                "useTemplate": "Template",
            }
        }