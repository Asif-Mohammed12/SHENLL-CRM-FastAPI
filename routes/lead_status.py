from fastapi import Body, APIRouter
from database.database import *
from schemas.lead_status import Response,UpdateLeadStatus

router = APIRouter()

@router.get("/", response_description="Leadstatus retrieved", response_model=Response)
async def get_leadsstatus():
    leads = await retrieve_leadstatus()
    return Response(
        status_code=200,
        status="ok",
        message="Leads record(s) found",
        data=leads
    )

@router.post("/", response_description="LeadStatus created", response_model=Response)
async def add_new_lead(new_leadstatus: LeadStatus = Body(...)):
    leadstatus = await add_leadstatus(new_leadstatus)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "LeadStatus record(s) created",
        "data": leadstatus,
    }

@router.put("/{id}", response_model=Response)
async def update_leadstatus(id: PydanticObjectId, req: UpdateLeadStatus = Body(...)):
    updated_leadstatus = await update_leadstatus_data(id, req.dict())
    if updated_leadstatus:
        return Response(
            status_code=200,
            status="ok",
            message="Leadstatus updated sucessfully",
            data= updated_leadstatus
        )
    return Response(
            status_code=400,
            status="error",
            message="Bad request"       
    )
