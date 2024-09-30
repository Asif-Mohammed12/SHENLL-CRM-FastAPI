from fastapi import APIRouter, Body, Query
from typing import Optional, List
from database.database import *
from pydantic import EmailStr
from schemas.staff import Response, UpdateStaffModel
from fastapi.responses import FileResponse
import json

router = APIRouter()

# @router.get("/", response_description="Staff retrieved", response_model=Response)
# async def get_staff():
#     staff = await retrieve_staff()
#     return {
#         "status_code": 200,
#         "status": "ok",
#         "response_type": "success",
#         "message": "Staff record(s) found",
#         "data": staff,
#     }

@router.get("/{id}", response_description="Student data retrieved", response_model=Response)
async def get_staff_data(id: PydanticObjectId):
    staff = await retrieve_staffs(id)
    if staff:
        # Add the image URL to the response data if the profileImage is present
        if staff.profileImage:
            staff.profileImage = f"/staff_images/{os.path.basename(staff.profileImage)}"
        return {
            "status_code": 200,
            "status": "ok",
            "message": "Staff data retrieved successfully",
            "data": staff,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Staff doesn't exist",
    }
# async def get_staff_data(id: PydanticObjectId):
#     staff = await retrieve_staffs(id)
#     if staff:
#         return {
#             "status_code": 200,
#             "status": "ok",
#             "message": "Staff data retrieved successfully",
#             "data": staff,
#         }
#     return {
#         "status_code": 404,
#         "response_type": "error",
#         "description": "staff doesn't exist",
#     }

@router.post("/", response_description="Staff created", response_model=Response)
# async def add_new_staff(
#     staffs: Staffs = Body(...),
#     profileImage: UploadFile = File(...)  # Optional image upload
# ):
#     staff = await add_staff(staffs, profileImage)
#     return {
#         "status_code": 200,
#         "status": "ok",
#         "response_type": "success",
#         "message": "Staff record(s) created",
#         "data": {
#             "_id": str(staff.id),
#             "createdAt": staff.createdAt
#         },
#     }
async def add_new_staff(new_staff: Staffs = Body(...)):
    staff = await add_staff(new_staff)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "Staff record(s) created",
        "data": {
            "_id": str(staff.id),
            "createdAt": staff.createdAt        
        },
    }

@router.put("/{id}", response_model=Response)
async def update_staff(id: PydanticObjectId, req: UpdateStaffModel = Body(...)):
    updated_staff = await update_staff_data(id, req.dict())
    if updated_staff:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "Staffs with ID: {} updated".format(id),
            "data": {
            "_id": str(updated_staff.id),
            "createdAt": updated_staff.updatedAt
        
        },
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Staffs with ID: {} not found".format(id),
        "data": False,
    }

@router.delete("/{id}", response_description="Staff data deleted from the database")
async def delete_staff_data(id: PydanticObjectId):
    deleted_staff = await delete_staff(id)
    if deleted_staff:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "Staff with ID: {} removed".format(id),
            "data": deleted_staff,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Staff with id {0} doesn't exist".format(id),
        "data": False,
    }

@router.get("/", response_description="Staff retrieved", response_model=Response)
async def get_staff( page: int = Query(1), limit: int = Query(10),
    name: Optional[str] = Query(None, description="Filter by staff name"),
    email: Optional[EmailStr] = Query(None, description="Filter by staff email"),
    mobile_number: Optional[str] = Query(None, description="Filter by staff mobile number")
):
    staff = await retrieve_staffsq(page=page,limit=limit,name=name, email=email, mobile_number=mobile_number)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "Staff record(s) found",
        "data": staff,
    }

