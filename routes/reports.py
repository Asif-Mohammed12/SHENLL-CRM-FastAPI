from fastapi import APIRouter, Body, Query
from database.database import *
from schemas.reports import Response, UpdateReports


router = APIRouter()

@router.get("/", response_description="reports retrieved", response_model=Response)
async def get_reports():
    reports = await retrieve_reports()
    # print("___________")
    # print(reports)
    # print("___________")
    return Response(
        status_code=200,
        status="ok",
        message="reports record(s) found",
        data=reports
    )

@router.get("/{id}", response_description="reports data retrieved", response_model=Response)
async def get_reports_data(id: PydanticObjectId):
    reports = await retrieve_report(id)
    if reports:
        return Response(
        status_code=200,
        status="ok",
        message="reports record(s) found",
        data=reports
    )
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "reports doesn't exist",
    }



@router.post("/", response_description="reports created", response_model=Response)
async def add_new_reports(new_reports: Reports = Body(...)):
    reports = await add_reports(new_reports)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "reports record(s) created",
        "data": reports,
    }

@router.put("/{id}", response_model=Response)
async def update_reports(id: PydanticObjectId, req: UpdateReports = Body(...)):
    updated_reports = await update_reports_data(id, req.dict())
    if updated_reports:
        return {
            "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "reports record(s) created",
        "data": updated_reports
        }
    return Response(
            status_code=400,
            status="error",
            message="Bad request"       
    )

@router.delete("/{id}", response_description="reports data deleted from the database")
async def delete_reports_data(id: PydanticObjectId):
    deleted_reports = await delete_reports(id)
    if deleted_reports:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "reports data retrieved successfully",
            "data": deleted_reports,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "reports with id {0} doesn't exist".format(id),
        "data": False,
    }
