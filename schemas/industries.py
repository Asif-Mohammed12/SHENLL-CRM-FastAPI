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
                "message": "industry record(s) found",
                "data": [
                    {
                        "industry": "Development",
                        "status": "ACTIVE"
                    }
                ]
            }
        }

class UpdateIndustry(BaseModel):
    industry:str
    status:str = "ACTIVE"
    createdAt:datetime = Field(default_factory=datetime.utcnow)
    updatedAt:datetime = Field(default_factory=datetime.utcnow)


    class Config:
        json_schema_extra = {
            "example": {
                "industry": "BPO",
            }
        }