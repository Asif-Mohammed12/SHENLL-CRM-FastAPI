from fastapi import APIRouter, Body

from database.database import *
# from models.student import Student
# from schemas.student import Response, UpdateStudentModel
from schemas.user import Response

router = APIRouter()

@router.get("/", response_description="Students retrieved", response_model=Response)
async def get_users():
    users = await retrieve_users()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Students data retrieved successfully",
        "data": users,
    }
