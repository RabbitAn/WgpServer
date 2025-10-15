from services.user_service import UserIn, UserOut, query_user_service, create_user_service, update_user_service, delete_user_service,UserUpdate,UserAddIn
from services.auth_services.dependencies import verify_access_token
from fastapi import APIRouter, Depends, HTTPException, status
import logging.config
from settings import LOGGER_CONFIG


logging.config.dictConfig(LOGGER_CONFIG)
logger = logging.getLogger(__name__)

user_router=APIRouter()

#查询用户
@user_router.get("users",summary="查询用户")
async def get_users(user_input: UserIn = Depends()):
    result= await query_user_service(user_input)
    print(result)
    return result

#创建用户
@user_router.post("users",summary="创建用户")
async def create_users(user_input: UserAddIn,payload:dict = Depends(verify_access_token(["admin"]))):
    try:
        logger.info(f"{payload['sub']}创建用户")
        return await create_user_service(user_input)
    except Exception as e:
        logger.error(f"创建用户失败: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

#更新用户
@user_router.put("users/{user_id}",summary="更新用户信息")
async def update_users(user_id: str, user_input: UserUpdate,payload:dict=Depends(verify_access_token(["admin"]))):
    try:
        logger.info(f"{payload['sub']}更新用户{user_id}信息")
        return await update_user_service(user_id, user_input)
    except Exception as e:
        logger.error(f"更新用户{user_id}信息失败: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


#删除用户
@user_router.delete("users/{user_id}",summary="删除用户")
async def delete_users(user_id: str,payload:dict=Depends(verify_access_token(["admin"]))):
    try:
        logger.info(f"{payload['sub']}删除用户{user_id}")
        return await delete_user_service(user_id)
    except Exception as e:
        logger.error(f"删除用户{user_id}失败: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
