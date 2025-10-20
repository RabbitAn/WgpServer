from uuid import UUID
import tortoise
import aerich.models
from fastapi import  APIRouter,Depends,status
from starlette.exceptions import HTTPException
from services.role_service import RoleOut, query_role_service, create_role_service, update_role_service, delete_role_service,RoleIn,RoleAddIn
from services.auth_services.dependencies import verify_access_token
import logging

logger = logging.getLogger(__name__)


role_router = APIRouter()
#TODO:查询角色列表,需要operator权限,传入角色信息，返回角色列表
@role_router.get("/roles",summary="查询角色列表")
async def get_role(role_input: RoleIn=Depends(),payload: dict=Depends(verify_access_token(["operator","engineer","admin"]))):
    try:
        logger.info(f"{payload['sub']}查询角色列表")
        results =await query_role_service(role_input)
        return results
    except Exception as e:
        logger.error(f"{payload['sub']}查询角色列表失败:{str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

#TODO:创建角色,需要管理员权限,传入角色信息，返回角色信息
@role_router.post("/roles/create",summary="创建角色")
async def create_roles(input: RoleAddIn,payload: dict=Depends(verify_access_token(["admin"]))):
    try:
        logger.info(f"{payload['sub']}创建角色")
        result = await create_role_service(input)
        return result
    except Exception as e:
        logger.error(f"{payload['sub']}创建角色失败:{str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


#TODO:更新角色,需要管理员权限,传入角色id和角色信息，返回角色信息
@role_router.put("/roles/{id}",summary="更新角色")
async def update_role(id:str, input: RoleIn,payload: dict=Depends(verify_access_token(["admin"]))):
    try:
        logger.info(f"{payload['sub']}更新角色")
        result = await update_role_service(id, input)
        return result
    except Exception as e:
        logger.error(f"{payload['sub']}更新角色失败:{str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))




#TODO:删除角色,需要管理员权限,传入角色id，返回成功或失败
@role_router.delete("/roles/{id}",summary="删除角色")
async def delete_role(id: str,payload: dict=Depends(verify_access_token(["admin"]))):
    try:
        logger.info(f"{payload['sub']}删除角色")
        result = await delete_role_service(id)
        return result
    except Exception as e:
        logger.error(f"{payload['sub']}删除角色失败:{str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))