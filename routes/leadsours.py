from fastapi import Body, APIRouter
from database.database import *
from schemas.leadsours import Response, UpdateLeadSource

router = APIRouter()

@router.get("/", response_description="Leadsource retrieved", response_model=Response)
async def get_leadsstatus():
    leads = await retrieve_leadsource()
    return Response(
        status_code=200,
        status="ok",
        message="Leadsource record(s) found",
        data=leads
    )

@router.post("/", response_description="LeadSource created", response_model=Response)
async def add_new_lead(new_leadsource: LeadStatus = Body(...)):
    leadsource = await add_leadsource(new_leadsource)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "LeadStatus record(s) created",
        "data": leadsource,
    }

@router.put("/{id}", response_model=Response)
async def update_leadsource(id: PydanticObjectId, req: UpdateLeadSource = Body(...)):
    updated_leadsource = await update_leadsource_data(id, req.dict())
    if updated_leadsource:
        return Response(
            status_code=200,
            status="ok",
            message="Leads updated sucessfully",
            data= updated_leadsource
        )
    return Response(
            status_code=400,
            status="error",
            message="Bad request"       
    )