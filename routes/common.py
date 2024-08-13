from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import List
import shutil
import os

router = APIRouter()

# Define the directory to save the uploaded files
UPLOAD_DIRECTORY = r"C:\Users\shnla\OneDrive\Desktop\CRM FASTAPI\fastapi-mongo\uploads"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@router.post("/fileUploads")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Prepare the response
        response = {
            "status": "ok",
            "message": "file created successfully",
            "data": {
                "originalname": file.filename,
                "filename": file.filename,
                "path": file_location,
                "size": os.path.getsize(file_location)
            }
        }

        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
