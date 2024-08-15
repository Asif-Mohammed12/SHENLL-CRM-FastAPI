from pydantic import BaseModel, Field
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
                "message": "Jobtitle record(s) found",
                "data": [
                    {
                        "jobTitle": "Development",
                        "status": "ACTIVE"
                    }
                ]
            }
        }

class UpdateJobdetials(BaseModel):
    jobTitle:str
    status:str = "ACTIVE"
    createdAt:datetime = Field(default_factory=datetime.utcnow)
    updatedAt:datetime = Field(default_factory=datetime.utcnow)


    class Config:
        json_schema_extra = {
            "example": {
                "jobTitle": "Python Developer",
            }
        }