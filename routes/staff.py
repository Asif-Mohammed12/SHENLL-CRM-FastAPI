from fastapi import APIRouter, Body

from database.database import *

from schemas.staff import Response
# from schemas.
router = APIRouter()

@router.get("/", response_description="Staff retrieved", response_model=Response)
async def get_staff():
    staff = await retrieve_staff()
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "Staff record(s) found",
        "data": staff,
    }

@router.post("/", response_description="Staff created", response_model=Response)
async def add_new_staff(new_staff: Staffs = Body(...)):
    staff = await add_staff(new_staff)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "Staff record(s) created",
        "data": staff,
    }