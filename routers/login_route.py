from services.login_services import login_service,login_out_service
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.auth_services.dependencies import bearer_auth


class LoginModel(BaseModel):
    username: str
    password: str

login_router = APIRouter()

#TODO:添加登录接口
@login_router.post("/login")
async def login(login_model: LoginModel,)->dict:
        return await login_service(login_model.username, login_model.password)


@login_router.post("/login_out")
async def login_out(token: str=Depends(bearer_auth))->dict:
        return await login_out_service(token)
