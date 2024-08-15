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
                "message": "Countries record(s) found",
                "data": [
                    {
                        "cca2": "cy"
                    }
                ]
            }
        }


class UpdateCountries(BaseModel):
    cca2:str


    class Config:
        json_schema_extra = {
            "example": {
                "cca2": "cy"
            }
        }