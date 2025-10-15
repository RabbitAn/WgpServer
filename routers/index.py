

#routerapi全部汇总
from fastapi import APIRouter
from routers.user_route import user_router
from routers.role_route import role_router
from routers.login_route import login_router

api_router = APIRouter()


api_router.include_router(user_router, prefix="/user", tags=["用户管理"])
api_router.include_router(role_router, prefix="/role", tags=["角色管理"])
api_router.include_router(login_router, tags=["用户登录"])


