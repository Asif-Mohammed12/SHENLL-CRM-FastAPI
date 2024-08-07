from fastapi import Body, APIRouter, HTTPException
from passlib.context import CryptContext
from datetime import datetime
from fastapi.responses import JSONResponse
import random

from auth.jwt_handler import sign_jwt
from database.database import add_admin
from models.admin import Admin
from models.opts import OTP
from schemas.admin import AdminData, AdminSignIn,OTPResponse, AdminOTPVerification 

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])


def generate_otp() -> str:
    """Generates a 4-digit OTP."""
    return f"{random.randint(1000, 9999)}"


@router.post("/login", response_model=OTPResponse)
async def admin_login(admin_credentials: AdminSignIn = Body(...)):
    # Find the admin by email
    admin = await Admin.find_one(Admin.email == admin_credentials.email)
    if not admin:
        raise HTTPException(status_code=403, detail="Incorrect email or password")

    # Verify the password
    if not hash_helper.verify(admin_credentials.password, admin.password):
        raise HTTPException(status_code=403, detail="Incorrect email or password")

    # Deactivate any existing active OTPs
    existing_otp = await OTP.find_one(
        OTP.email == admin_credentials.email,
        OTP.status == "ACTIVE"
    )
    if existing_otp:
        existing_otp.status = "INACTIVE"
        existing_otp.updatedAt = datetime.utcnow()
        await existing_otp.save()

    # Generate a new OTP
    # otp_code = generate_otp()
    otp_code ="1234"
    # Store the new OTP in the database
    new_otp = OTP(
        email=admin_credentials.email,
        code=otp_code,
        type="LOGIN",
        status="ACTIVE",
        createdAt=datetime.utcnow(),
        updatedAt=datetime.utcnow()
    )
    await new_otp.insert()

    # Send the OTP to the user's email
    # try:
    #     send_otp_email(admin_credentials.email, otp_code)
    # except Exception as e:
    #     # Log the error and return an appropriate response
    #     # logger.error(f"Failed to send OTP email: {str(e)}")
    #     raise HTTPException(status_code=500, detail="Failed to send OTP. Please try again later.")

    # Return the response
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "message": "OTP sent successfully",
            "data": {
                "email": admin_credentials.email,
                "type": "LOGIN"
            }
        }
    )

@router.post("/verifyOtp")
async def verify_otp(otp_details: AdminOTPVerification = Body(...)):
    otp_record = await OTP.find_one(OTP.email == otp_details.email, OTP.status == "ACTIVE")
    if otp_record:
        if otp_record.code == otp_details.code:
            otp_record.status = "INACTIVE"
            otp_record.updatedAt = datetime.utcnow()
            await otp_record.save()

            # Generate JWT token
            jwt_token = sign_jwt(otp_details.email)

            return JSONResponse(
                status_code=200,
                content={
                    "status": "ok",
                    "message": "User verified successfully",
                    "data": {
                        "token": jwt_token["access_token"]
                    }
                }
            )

        # OTP is incorrect
        raise HTTPException(status_code=403, detail="Incorrect OTP")

    # No active OTP record found
    raise HTTPException(status_code=404, detail="Active OTP record not found")
  
@router.post("/create_admin", response_model=AdminData)
async def admin_signup(admin: Admin = Body(...)):
    admin_exists = await Admin.find_one(Admin.email == admin.email)
    if admin_exists:
        raise HTTPException(
            status_code=409, detail="Admin with email supplied already exists"
        )

    admin.password = hash_helper.encrypt(admin.password)
    new_admin = await add_admin(admin)
    return AdminData(
        name=new_admin.name,
        email=new_admin.email,
        mobileNumber=new_admin.mobileNumber,
        role=new_admin.role,
        status=new_admin.status,
        createdDate=new_admin.createdDate,
        updatedDate=new_admin.updatedDate,
    )
