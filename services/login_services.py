from services.auth_services.jwt_handler import create_access_token, decode_access_token
from fastapi import HTTPException, status
from settings import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from models.user import User
from jose import JWTError

#TODO:登录传入用户名密码，返回token，token有效期为ACCESS_TOKEN_EXPIRE_MINUTES分钟和用户信息
async def login_service(username:str, password:str):
    user = await User.get_or_none(username=username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="用户不存在")
    if not user.check_password(password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="密码错误")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username,"role": user.role}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "username": user.username, "role": user.role}


#TODO:登出
async  def login_out_service(token:str):
    try:
        payload = decode_access_token(token)
        if not payload:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token无效")
        return {"msg": "登出成功"}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token无效")

