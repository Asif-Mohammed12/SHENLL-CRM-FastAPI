from fastapi import Body, APIRouter, HTTPException
from passlib.context import CryptContext
from datetime import datetime
from fastapi.responses import JSONResponse
import random
from schemas.leads import Response
from database.database import *



router = APIRouter()

@router.get("/", response_description="organization retrieved", response_model=Response)
async def get_leads():
    leads = await retrieve_leads()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "organization data retrieved successfully",
        "data": Leads
    }