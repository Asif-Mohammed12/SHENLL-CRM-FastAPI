from fastapi import APIRouter, Body, Query
from database.database import *
from schemas.departments import Response, UpdateDepartment


router = APIRouter()

@router.get("/", response_description="Tasks retrieved", response_model=Response)
async def get_depart():
    department = await retrieve_departments()
    return Response(
        status_code=200,
        status="ok",
        message="department record(s) found",
        data=department
    )

@router.get("/{id}", response_description="Task data retrieved", response_model=Response)
async def get_departments_data(id: PydanticObjectId):
    department = await retrieve_department(id)
    if department:
        return Response(
        status_code=200,
        status="ok",
        message="department record(s) found",
        data=department
    )
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "department doesn't exist",
    }



@router.post("/", response_description="department created", response_model=Response)
async def add_new_department(new_department: Departments = Body(...)):
    department = await add_department(new_department)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "department record(s) created",
        "data": {
            "_id": str(department.id),
            "createdAt": department.createdAt
        
        },
    }

@router.put("/{id}", response_model=Response)
async def update_department(id: PydanticObjectId, req: UpdateDepartment = Body(...)):
    updated_department = await update_department_data(id, req.dict())
    if updated_department:
        return {
            "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "department record(s) created",
            "data": {
            "_id": str(updated_department.id),
            "createdAt": updated_department.updatedAt
        
        },
        }
    return Response(
            status_code=400,
            status="error",
            message="Bad request"       
    )

@router.delete("/{id}", response_description="department data deleted from the database")
async def delete_department_data(id: PydanticObjectId):
    deleted_department = await delete_task(id)
    if deleted_department:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "department data retrieved successfully",
            "data": deleted_department,
        }
    return Response(
            status_code=400,
            status="Bad request",
            message="department with id {0} doesn't exist".format(id)      
    )
    # return {
    #     "status_code": 404,
    #     "response_type": "error",
    #     "description": "Leads with id {0} doesn't exist".format(id),
    #     "data": False,
    # }
