from fastapi import APIRouter, Body, Query
from database.database import *
from schemas.industries import Response, UpdateIndustry


router = APIRouter()

@router.get("/", response_description="industries retrieved", response_model=Response)
async def get_industries():
    industries = await retrieve_industries()
    # print("___________")
    # print(industries)
    # print("___________")
    return Response(
        status_code=200,
        status="ok",
        message="industries record(s) found",
        data=industries
    )

@router.get("/{id}", response_description="industries data retrieved", response_model=Response)
async def get_industries_data(id: PydanticObjectId):
    industries = await retrieve_industrie(id)
    if industries:
        return Response(
        status_code=200,
        status="ok",
        message="industries record(s) found",
        data=industries
    )
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "industries doesn't exist",
    }



@router.post("/", response_description="industries created", response_model=Response)
async def add_new_industries(new_industries: Industries = Body(...)):
    industries = await add_industries(new_industries)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "industries record(s) created",
        "data": {
            "_id": str(industries.id),
            "createdAt": industries.createdAt
        
        },
    }

@router.put("/{id}", response_model=Response)
async def update_industries(id: PydanticObjectId, req: UpdateIndustry = Body(...)):
    updated_industries = await update_industries_data(id, req.dict())
    if updated_industries:
        return {
            "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "industries record(s) created",
            "data": {
            "_id": str(updated_industries.id),
            "createdAt": updated_industries.updatedAt
        
        },
        }
    return Response(
            status_code=400,
            status="error",
            message="Bad request"       
    )

@router.delete("/{id}", response_description="industries data deleted from the database")
async def delete_industries_data(id: PydanticObjectId):
    deleted_industries = await delete_industrie(id)
    if deleted_industries:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "industries data retrieved successfully",
            "data": deleted_industries,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "industries with id {0} doesn't exist".format(id),
        "data": False,
    }
