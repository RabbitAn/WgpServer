from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer,HTTPBearer,HTTPAuthorizationCredentials
from services.auth_services. jwt_handler import decode_access_token
from typing import List


bearer_auth = HTTPBearer()

# TODO定义一个依赖，获取当前用户的 username 或用户ID
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


#TODO获取当前用户的 username 或用户ID
def get_current_user(token: HTTPAuthorizationCredentials = Depends(bearer_auth)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return payload




#TODO写一个装饰器，验证当前用户是否有权限访问某个 API
def verify_access_token(role_names:List[str]):
   def wrapper(payload:dict=Depends(get_current_user)):
       for role in role_names:
           if payload.get("role") == role:

               return payload
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="禁止访问")
   return wrapper
