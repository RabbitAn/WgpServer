from settings import  SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta,datetime,UTC
from typing import Optional
from jose import jwt, JWTError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials







#TODO创建token, 传入数据, 过期时间, 返回token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy() # dict.copy() 方法用于复制字典，返回一个字典的浅拷贝。
    if expires_delta: # expires_delta 是一个可选参数，如果没有传入，则使用默认的有效期
        expire = datetime.now(UTC) + expires_delta # UTC时间
    else:
        expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)# 默认有效期8天
    to_encode.update({"exp": expire})# 更新字典，增加"exp"字段，值为当前时间加上有效期
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)# 加密token
    return encoded_jwt # 返回token字符串



#TODO解密token, 传入token, 返回数据
def decode_access_token(token:HTTPAuthorizationCredentials ):
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])# 解密token
        return payload
    except JWTError:
        return None
