from fastapi import APIRouter, Body

from database.database import *
# from models.student import Student
# from schemas.student import Response, UpdateStudentModel
from schemas.user import Response,UpdateUserModel

router = APIRouter()

@router.get("/", response_description="user retrieved", response_model=Response)
async def get_users():
    users = await retrieve_users()
    return {
        "status_code": 200,
        "status": "ok",
        "message": "Students data retrieved successfully",
        "data": users,
    }

@router.get("/{id}", response_description="user data retrieved", response_model=Response)
async def get_user_data(id: PydanticObjectId):
    user = await retrieve_user(id)
    if user:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "User data retrieved successfully",
            "data": user,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "staff doesn't exist",
    }

@router.post("/", response_description="User created", response_model=Response)
async def add_new_user(new_user: User = Body(...)):
    user = await add_user(new_user)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "User record(s) created",
        "data": user,
    }

@router.put("/{id}", response_model=Response)
async def update_staff(id: PydanticObjectId, req: UpdateUserModel = Body(...)):
    updated_user = await update_user_data(id, req.dict())
    if updated_user:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "User with ID: {} updated".format(id),
            "data": updated_user,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Staffs with ID: {} not found".format(id),
        "data": False,
    }

@router.delete("/{id}", response_description="Staff data deleted from the database")
async def delete_user_data(id: PydanticObjectId):
    deleted_user = await delete_user(id)
    if deleted_user:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "Staff with ID: {} removed".format(id),
            "data": deleted_user,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Staff with id {0} doesn't exist".format(id),
        "data": False,
    }