from fastapi import APIRouter, Body, Query
from database.database import *
from schemas.emails import Response, UpdateEmails


router = APIRouter()

@router.get("/", response_description="emails retrieved", response_model=Response)
async def get_emails():
    emails = await retrieve_emails()
    # print("___________")
    # print(emails)
    # print("___________")
    return Response(
        status_code=200,
        status="ok",
        message="emails record(s) found",
        data=emails
    )

@router.get("/{id}", response_description="emails data retrieved", response_model=Response)
async def get_emails_data(id: PydanticObjectId):
    emails = await retrieve_email(id)
    if emails:
        return Response(
        status_code=200,
        status="ok",
        message="emails record(s) found",
        data=emails
    )
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "emails doesn't exist",
    }



@router.post("/", response_description="emails created", response_model=Response)
async def add_new_emails(new_emails: Emails = Body(...)):
    emails = await add_email(new_emails)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "emails record(s) created",
        "data": emails,
    }

@router.put("/{id}", response_model=Response)
async def update_emails(id: PydanticObjectId, req: UpdateEmails = Body(...)):
    updated_emails = await update_email_data(id, req.dict())
    if updated_emails:
        return {
            "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "emails record(s) created",
        "data": updated_emails
        }
    return Response(
            status_code=400,
            status="error",
            message="Bad request"       
    )

@router.delete("/{id}", response_description="emails data deleted from the database")
async def delete_emails_data(id: PydanticObjectId):
    deleted_emails = await delete_email(id)
    if deleted_emails:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "emails data retrieved successfully",
            "data": deleted_emails,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "emails with id {0} doesn't exist".format(id),
        "data": False,
    }
