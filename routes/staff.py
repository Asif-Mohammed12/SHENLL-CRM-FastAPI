from fastapi import APIRouter, Body

from database.database import *

from schemas.staff import Response
# from schemas.
router = APIRouter()

@router.get("/", response_description="Staff retrieved", response_model=Response    )
async def get_staff():
    staff = await retrieve_staff()
    # print("staff", staff)
    return {
        "status_code":200,
        "status": "ok",
        "response_type": "success",
        "message": "Staff record(s) found",
        "data": staff,
    }
