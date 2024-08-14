from fastapi import Body, APIRouter
from database.database import *
from models.organizations import Organizations
from schemas.organizations import Response,UpdateOrganizationModel

router = APIRouter()


@router.post('/')
async def addOrganization(organization:Organizations = Body(...)):
    new_organizations = await add_organizations(organization)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "organization created successfully",
        "data": new_organizations,
    }

@router.get("/", response_description="organization retrieved", response_model=Response)
async def get_organization():
    organization = await retrieve_organizations()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "organization data retrieved successfully",
        "data": organization,
    }

@router.put("/{id}", response_model=Response)
async def put_organization(id:PydanticObjectId,req:UpdateOrganizationModel = Body(...)):
    updated_organization = await update_organization_data(id, req.dict())
    if updated_organization:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "organization with ID: {} updated".format(id),
            "data": updated_organization,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. organization with ID: {} not found".format(id),
        "data": False,
    }

@router.delete("/{id}")
async def deleteorganization(id:PydanticObjectId):
    delete_organizations = await delete_organization(id)
    if delete_organizations:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "organization with ID: {} removed".format(id),
            "data": delete_organizations,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "organization with id {0} doesn't exist".format(id),
        "data": False,
    }