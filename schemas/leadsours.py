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
                "message": "Leadsource record(s) found",
                "data": [
                    {
                        "leadStatus": "NEW",
                        "displayIndex": "1",
                        "status": "ACTIVE"
                    }
                ]
            }
        }

class UpdateLeadSource(BaseModel):
    leadSoure:str
    status:str = "ACTIVE"
    displayIndex:str
    createdAt:datetime = Field(default_factory=datetime.utcnow)
    updatedAt:datetime = Field(default_factory=datetime.utcnow)


    class Config:
        json_schema_extra = {
            "example": {
                "leadSoure": "developer",
                "displayIndex":"3",

            }
        }