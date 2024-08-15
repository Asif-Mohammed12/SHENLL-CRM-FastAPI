from fastapi import APIRouter, Body, Query
from database.database import *
from schemas.jobtitles import Response, UpdateJobdetials


router = APIRouter()

@router.get("/", response_description="jobtitles retrieved", response_model=Response)
async def get_jobtitles():
    jobtitles = await retrieve_jobtitles()
    # print("___________")
    # print(jobtitles)
    # print("___________")
    return Response(
        status_code=200,
        status="ok",
        message="jobtitles record(s) found",
        data=jobtitles
    )

@router.get("/{id}", response_description="jobtitles data retrieved", response_model=Response)
async def get_jobtitles_data(id: PydanticObjectId):
    jobtitles = await retrieve_jobtitle(id)
    if jobtitles:
        return Response(
        status_code=200,
        status="ok",
        message="jobtitles record(s) found",
        data=jobtitles
    )
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "jobtitles doesn't exist",
    }



@router.post("/", response_description="jobtitles created", response_model=Response)
async def add_new_jobtitles(new_jobtitles: Jobtitles = Body(...)):
    jobtitles = await add_jobtitles(new_jobtitles)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "jobtitles record(s) created",
        "data": jobtitles,
    }

@router.put("/{id}", response_model=Response)
async def update_jobtitles(id: PydanticObjectId, req: UpdateJobdetials = Body(...)):
    updated_jobtitles = await update_jobtitles_data(id, req.dict())
    if updated_jobtitles:
        return {
            "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "jobtitles record(s) created",
        "data": updated_jobtitles
        }
    return Response(
            status_code=400,
            status="error",
            message="Bad request"       
    )

@router.delete("/{id}", response_description="jobtitles data deleted from the database")
async def delete_jobtitles_data(id: PydanticObjectId):
    deleted_jobtitles = await delete_jobtitles(id)
    if deleted_jobtitles:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "jobtitles data retrieved successfully",
            "data": deleted_jobtitles,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "jobtitles with id {0} doesn't exist".format(id),
        "data": False,
    }
