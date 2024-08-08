from fastapi import FastAPI, Depends

from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.admin import router as AdminRouter
from routes.student import router as StudentRouter
from routes.user import router as UserRouter
from routes.organizations import router as Orgrouter
from routes.leads import router as Leadsrouter

app = FastAPI()

token_listener = JWTBearer()


@app.on_event("startup")
async def on_startup():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/api/v1/auth")
# app.include_router(StudentRouter,tags=["Students"],prefix="/student",dependencies=[Depends(token_listener)],)
app.include_router(UserRouter,tags=["users"],prefix="/users")
app.include_router(Leadsrouter,tags=["leads"],prefix="/leads")
app.include_router(Orgrouter,tags=["organization"],prefix="/organization")
