from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from beanie import PydanticObjectId
from beanie import Document

class TaskModel(Document):
    leadName: str
    subject: str
    relatedTo: str
    contactPerson: str
    startDate: str
    dueDate: str
    priority: str
    description: str
    status: str = "ACTIVE"
    createdAt: datetime = Field(default_factory=datetime.now)
    updatedAt: datetime = Field(default_factory=datetime.now)
    leadsId: Optional[PydanticObjectId] = None
    assignedTo: Optional[PydanticObjectId] = None

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "leadName": "leadName",
                "subject": "subject",
                "relatedTo": "relatedTo",
                "contactPerson": "contactPerson",
                "startDate": "2024-01-01T00:00:00",
                "dueDate": "2024-01-31T23:59:59",
                "priority": "priority",
                "description": "description",
                "status": "Active",
                "createdAt": "2024-01-01T00:00:00",
                "updatedAt": "2024-01-01T00:00:00"
            }
        }

    class Settings:
        name = "tasks"
