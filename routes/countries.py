from fastapi import APIRouter, Body, Query
from database.database import *
from schemas.countries import Response


router = APIRouter()


@router.get("/", response_description="countries retrieved", response_model=Response)
async def get_countries():
    countries = await retrieve_countries()
    return Response(
        status_code=200,
        status="ok",
        message="countries record(s) found",
        data=countries
    )

# @router.post("/", response_description="countries created", response_model=Response)
# async def add_new_countries(new_countries: Departments = Body(...)):
#     countries = await add_countries(new_countries)
#     return {
#         "status_code": 200,
#         "status": "ok",
#         "response_type": "success",
#         "message": "countries record(s) created",
#         "data": countries,
    # }