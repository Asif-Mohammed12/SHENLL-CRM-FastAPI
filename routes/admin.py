from fastapi import Body, APIRouter, HTTPException
from passlib.context import CryptContext
from datetime import datetime
from fastapi.responses import JSONResponse
import random

from auth.jwt_handler import sign_jwt
from database.database import add_admin
from models.admin import Admin
from models.opts import OTP
from schemas.admin import AdminData, AdminSignIn,OTPResponse, AdminOTPVerification,  ForgotPassword, ResetPassword

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])


def generate_otp() -> str:
    """Generates a 4-digit OTP."""
    return f"{random.randint(1000, 9999)}"


@router.post("/user/login", response_model=OTPResponse)
async def admin_login(admin_credentials: AdminSignIn = Body(...)):
    admin_exists = await Admin.find_one(Admin.email == admin_credentials.email)
    if admin_exists:
        password_verified = hash_helper.verify(admin_credentials.password, admin_exists.password)
        if password_verified:
            # Check for existing active OTP
            existing_otp = await OTP.find_one(
                OTP.email == admin_credentials.email,
                OTP.status == "ACTIVE"
            )
            if existing_otp:
                # Set the existing OTP status to INACTIVE
                existing_otp.status = "INACTIVE"
                existing_otp.updatedAt = datetime.utcnow()
                await existing_otp.save()

            # Generate a new OTP
            otp_code = generate_otp()
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

            # Send the OTP to the user's email (implement email sending logic here)

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

        raise HTTPException(status_code=403, detail="Incorrect email or password")

    raise HTTPException(status_code=403, detail="Incorrect email or password")

@router.post("/user/verifyOtp")
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

@router.post("/user/signup", response_model=AdminData)
async def admin_signup(admin: Admin = Body(...)):
    admin_exists = await Admin.find_one(Admin.email == admin.email)
    if admin_exists:
        raise HTTPException(
            status_code=409, detail="Admin with email supplied already exists"
        )

    admin.password = hash_helper.encrypt(admin.password)
    admin.role="ADMIN"
    admin.status="ACTIVE"
    await add_admin(admin)
    otp_code = generate_otp()
            # Store the new OTP in the database
    new_otp = OTP(
        email=admin.email,
        code=otp_code,
        type="LOGIN",
        status="ACTIVE",
        createdAt=datetime.utcnow(),
        updatedAt=datetime.utcnow()
    )
    await new_otp.insert()
    return JSONResponse({
        "status": "ok",
        "message": "Otp sent successfully",
        "data": {
            "email": admin.email,
            "type": "signup"
    }
    })

@router.post('/user/forgotPassword',response_model=ForgotPassword)
async def forgotPassword(admin: ForgotPassword = Body(...)):
    admin_exists = await Admin.find_one(Admin.email == admin.email)
    if admin_exists:
        existing_otp = await OTP.find_one(
        OTP.email == admin.email,
        OTP.status == "ACTIVE"
        )
        if existing_otp:
        # Set the existing OTP status to INACTIVE
            existing_otp.status = "INACTIVE"
            existing_otp.updatedAt = datetime.utcnow()
            await existing_otp.save()
        
        otp_code = generate_otp()
        # Store the new OTP in the database
        new_otp = OTP(
        email=admin.email,
        code=otp_code,
        type="FPASSWORD",
        status="ACTIVE",
        createdAt=datetime.utcnow(),
        updatedAt=datetime.utcnow()
        )
        await new_otp.insert()
        
        return JSONResponse(
        status_code=200,
        content={
        "status": "ok",
            "message": "Otp sent successfully",
            "data": {
            "email": "ram@gmail.com",
        "type": "FPASSWORD"
                    }
        }
        )
    raise HTTPException(status_code=403, detail="Incorrect email or password")

@router.post('/user/resetPassword',response_model=ResetPassword)
async def reset_password(request: ResetPassword = Body(...)):
    code = request.code
    password = request.password
    email = request.email
    print("email",email)
    admin = await Admin.find_one(Admin.email == email)
    # print("admin_id", admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="User not found")
    otp_record = await OTP.find_one(OTP.email == email, OTP.status == "ACTIVE")

    if otp_record.code != code:
        raise HTTPException(status_code=404, detail="Incorrect OTP")
    
    encrypted_password = hash_helper.encrypt(password)
    
    admin.password = encrypted_password
    await admin.save()

    jwt_token = sign_jwt(email)
    
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "message": "User updated successfully",
            "data": {
                "token": jwt_token["access_token"]
            }
        }
    )