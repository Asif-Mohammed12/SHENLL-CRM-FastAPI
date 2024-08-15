from fastapi import APIRouter, Body, Query
from database.database import *
from schemas.roles import Response, UpdateRoles


router = APIRouter()

@router.post("/", response_description="roles created", response_model=Response)
async def add_new_role(new_role: Roles = Body(...)):
    roles = await add_role(new_role)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "roles record(s) created",
        "data": roles,
    }

@router.get("/", response_description="roles retrieved", response_model=Response)
async def get_roles():
    roles = await retrieve_roles()
    # print("___________")
    # print(roles)
    # print("___________")
    return Response(
        status_code=200,
        status="ok",
        message="roles record(s) found",
        data=roles
    )

@router.get("/{id}", response_description="roles data retrieved", response_model=Response)
async def get_roles_data(id: PydanticObjectId):
    roles = await retrieve_role(id)
    if roles:
        return Response(
        status_code=200,
        status="ok",
        message="reports record(s) found",
        data=roles
    )
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "roles doesn't exist",
    }

@router.put("/{id}", response_model=Response)
async def update_roles(id: PydanticObjectId, req: UpdateRoles = Body(...)):
    updated_roles = await update_roles_data(id, req.dict())
    if updated_roles:
        return {
            "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "roles record(s) created",
        "data": updated_roles
        }
    return Response(
            status_code=400,
            status="error",
            message="Bad request"       
    )

@router.delete("/{id}", response_description="roles data deleted from the database")
async def delete_roles_data(id: PydanticObjectId):
    deleted_roles = await delete_roles(id)
    if deleted_roles:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "roles data retrieved successfully",
            "data": deleted_roles,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "roles with id {0} doesn't exist".format(id),
        "data": False,
    }