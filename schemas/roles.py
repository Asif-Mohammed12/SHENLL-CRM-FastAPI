from beanie import Document
from pydantic import Field, EmailStr,BaseModel
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
                "status_code": 200,
                "status":"ok",
                "message": "Operation successful",
                "data": "Sample data",
            }
        }


class UpdateRoles(BaseModel):
    roleName:str
    class Config:
        json_schema_extra = {
            "example": {
                "roleName": "abdul",
            }
        }