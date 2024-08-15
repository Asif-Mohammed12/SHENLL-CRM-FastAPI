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
from routes.reports import router as ReportsRouter
from routes.roles import router as RolesRouter
from routes.organizations import router as OrgRouter
from routes.lead import router as LeadsRouter
from routes.emails import router as EmailsRouter
from routes.task import router as taskRouter
from routes.sms import router as SmsRouter
from routes.industries import router as IndustriesRouter
from routes.jobtitles import router as JobtitlesRouter
from routes.countries import router as CountriesRouter
from routes.leadsours import router as LeadSourceRouter
from routes.departments import router as DepartmentsRouter

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
app.include_router(CountriesRouter,tags=["countries"],prefix="/api/v1/countries")
app.include_router(SmsRouter,tags=["sms"],prefix="/api/v1/sms")
app.include_router(ReportsRouter,tags=["reports"],prefix="/api/v1/reports")
app.include_router(DepartmentsRouter,tags=["departments"],prefix="/api/v1/departments")
app.include_router(taskRouter,tags=["tasks"],prefix="/api/v1/task")
app.include_router(EmailsRouter,tags=["emails"],prefix="/api/v1/emails")
app.include_router(JobtitlesRouter,tags=["jobtitles"],prefix="/api/v1/jobtitles")
app.include_router(IndustriesRouter,tags=["industries"],prefix="/api/v1/industries")
app.include_router(LeadstatusRouter,tags=["leadstatus"],prefix="/api/v1/leadstatus")
app.include_router(LeadSourceRouter,tags=["leadsource"],prefix="/api/v1/leadsource")
app.include_router(OrgRouter,tags=["organization"],prefix="/api/v1/organization")
app.include_router(RolesRouter,tags=["roles"],prefix="/api/v1/roles")
app.include_router(CommonRouter,tags=["Files"],prefix="/api/v1")