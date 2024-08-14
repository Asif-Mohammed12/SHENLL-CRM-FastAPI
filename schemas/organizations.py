from pydantic import BaseModel
from typing import Optional, Any

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

class UpdateOrganizationModel(BaseModel):
    jobTitle: Optional[str]
    class Collection:
        name = "organizations"

    class Config:
        json_schema_extra = {
            "example": {
                "jobTitle": "developer",
            }
        }