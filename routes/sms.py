from fastapi import APIRouter, Body, Query
from database.database import *
from schemas.sms import Response, UpdateSms


router = APIRouter()

@router.get("/", response_description="sms retrieved", response_model=Response)
async def get_sms():
    sms = await retrieve_smses()
    # print("___________")
    # print(sms)
    # print("___________")
    return Response(
        status_code=200,
        status="ok",
        message="sms record(s) found",
        data=sms
    )

@router.get("/{id}", response_description="sms data retrieved", response_model=Response)
async def get_sms_data(id: PydanticObjectId):
    sms = await retrieve_sms(id)
    if sms:
        return Response(
        status_code=200,
        status="ok",
        message="sms record(s) found",
        data=sms
    )
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "sms doesn't exist",
    }



@router.post("/", response_description="sms created", response_model=Response)
async def add_new_sms(new_sms: Sms = Body(...)):
    sms = await add_sms(new_sms)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "sms record(s) created",
        "data": {
            "_id": str(sms.id),
            "createdAt": sms.createdAt
        
        },
    }

@router.put("/{id}", response_model=Response)
async def update_sms(id: PydanticObjectId, req: UpdateSms = Body(...)):
    updated_sms = await update_sms_data(id, req.dict())
    if updated_sms:
        return {
            "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "sms record(s) created",
            "data": {
            "_id": str(updated_sms.id),
            "createdAt": updated_sms.updatedAt
        
        },
        }
    return Response(
            status_code=400,
            status="error",
            message="Bad request"       
    )

@router.delete("/{id}", response_description="sms data deleted from the database")
async def delete_sms_data(id: PydanticObjectId):
    deleted_sms = await delete_sms(id)
    if deleted_sms:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "sms data retrieved successfully",
            "data": deleted_sms,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "sms with id {0} doesn't exist".format(id),
        "data": False,
    }
