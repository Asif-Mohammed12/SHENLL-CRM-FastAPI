from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.admin import router as AdminRouter
# from routes.student import router as StudentRouter
from routes.user import router as UserRouter
from routes.staff import router as StaffRouter
from routes.lead_status import router as LeadstatusRouter
from routes.common import router as CommonRouter
from routes.organizations import router as OrgRouter
from routes.lead import router as LeadsRouter
from routes.leadsours import router as LeadSourceRouter

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

token_listener = JWTBearer()


# CORS Middleware Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; adjust to specific origins for more security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods; adjust as needed
    allow_headers=["*"],  # Allow all headers; adjust as needed
)

@app.on_event("startup")
async def on_startup():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}
# 

app.include_router(AdminRouter, tags=["Administrator"], prefix="/api/v1/auth/user")
# app.include_router(StudentRouter,tags=["Students"],prefix="/student",dependencies=[Depends(token_listener)],)
app.include_router(UserRouter,tags=["Users"],prefix="/users")
app.include_router(StaffRouter,tags=["Staffs"],prefix="/api/v1/staff")
app.include_router(LeadsRouter,tags=["leads"],prefix="/api/v1/leads")
app.include_router(LeadstatusRouter,tags=["leadstatus"],prefix="/api/v1/leadstatus")
app.include_router(LeadSourceRouter,tags=["leadsource"],prefix="/api/v1/leadsource")
app.include_router(OrgRouter,tags=["organization"],prefix="/api/v1/organization")
app.include_router(CommonRouter,tags=["Files"],prefix="/api/v1")