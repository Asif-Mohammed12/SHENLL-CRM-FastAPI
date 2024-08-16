from fastapi import Body, APIRouter, HTTPException,Query
from passlib.context import CryptContext
from datetime import datetime
from fastapi.responses import JSONResponse
import random
from schemas.lead import Response,UpdateLead
from database.database import *



router = APIRouter()

@router.get("/", response_description="Leads retrieved", response_model=Response)
async def get_leads():
    leads = await retrieve_leads()
    return Response(
        status_code=200,
        status="ok",
        message="Leads record(s) found",
        data=leads
    )
# async def get_leads(
#     page: int = Query(1, ge=1, description="Page number"),
#     limit: int = Query(10, ge=1, le=100, description="Number of items per page")
# ):
#     leads = await retrieve_leads(page=page, limit=limit)
#     return Response(
#         status="ok",
#         message="Leads record(s) found",
#         data=leads
#     )

@router.get("/{id}", response_description="Lead data retrieved", response_model=Response)
async def get_lead_data(id: PydanticObjectId):
    leads = await retrieve_lead(id)
    if leads:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Leads data retrieved successfully",
            "data": leads,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Student doesn't exist",
    }



@router.post("/", response_description="Leads created", response_model=Response)
async def add_new_lead(new_lead: Leads = Body(...)):
    lead = await add_lead(new_lead)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "Lead record(s) created",
        "data": {
            "_id": str(lead.id),
            "createdAt": lead.createdAt
        
        },
    }

@router.put("/{id}", response_model=Response)
async def update_student(id: PydanticObjectId, req: UpdateLead = Body(...)):
    updated_lead = await update_lead_data(id, req.dict())
    if updated_lead:
        return {
            "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "Lead record(s) created",
            "data": {
            "_id": str(updated_lead.id),
            "createdAt": updated_lead.updatedAt
        
        },
        }
    return Response(
            status_code=400,
            status="error",
            message="Bad request"       
    )

@router.delete("/{id}", response_description="Leads data deleted from the database")
async def delete_lead_data(id: PydanticObjectId):
    deleted_lead = await delete_leads(id)
    if deleted_lead:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Leads with ID: {} removed".format(id),
            "data": deleted_lead,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Leads with id {0} doesn't exist".format(id),
        "data": False,
    }