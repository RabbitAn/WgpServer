import uuid
from models import role
from models.user import User
from models.role import Role
from models.user_role import UserRole
from pydantic import BaseModel
from typing import List, Optional
import datetime
from tortoise.transactions import in_transaction

class UserIn(BaseModel):
    username: Optional[str]=None
    email: Optional[str]=None
    role: Optional[str]=None
    phone: Optional[str]=None
    is_active: Optional[bool]=None
    page: Optional[int]=1
    page_size: Optional[int]=10

class UserOut(BaseModel):
    id: uuid.UUID
    username: str
    role:str
    email: Optional[str]=None
    phone: Optional[str]=None
    is_active: bool
    created_at: datetime.datetime


#用户条件查询
async def query_user_service(user: UserIn):
    count_total = await User.all().count()
    print("总记录数:", count_total)

    count_active = await User.filter(is_active=True).count()
    print("激活用户数:", count_active)

    count_inactive = await User.filter(is_active=False).count()
    print("未激活用户数:", count_inactive)
    query = User.all()  # 从全部开始
    if user.is_active is not None:  # 只有传了 is_active 才加条件
        query = query.filter(is_active=user.is_active)
    #判断是否有用户名
    if user.username:
        query = query.filter(username__icontains=user.username)
    #判断是否有邮箱
    if user.email:
        query = query.filter(email__icontains=user.email)
    #判断是否有手机号
    if user.phone:
        query = query.filter(phone__icontains=user.phone)
    if user.role:
        query = query.filter(role=user.role)
    #返回查询结果
    result=await query.all()
    #分页
    result=result[user.page_size*(user.page-1):user.page_size*user.page]

    # 使用解包转换成 UserOut
    users_out = []
    for db_user in result:
        user_out = UserOut(
            id=db_user.id,
            username=db_user.username,
            role=db_user.role,
            email=db_user.email,
            is_active=db_user.is_active,
            created_at=db_user.created_at
        )
        users_out.append(user_out)
    return {"total": count_total, "users": users_out,"page":user.page,"page_size":user.page_size}



class UserAddIn(BaseModel):
    username: Optional[str]
    email: Optional[str]=None
    role: Optional[str]
    password: Optional[str]
    phone: Optional[str]=None
    is_active: Optional[bool]=True

#用户新增
async def create_user_service(user_in: UserAddIn):
    async with in_transaction():
        # 创建用户对象
        user = await User.create(
            username=user_in.username,
            email=user_in.email,
            password=user_in.password,
            phone=user_in.phone,
            role=user_in.role,
            is_active=user_in.is_active
        )

        # 查找角色
        role = await Role.get_or_none(role_name=user_in.role)
        if not role:
            raise ValueError(f"角色 {user_in.role} 不存在")

        # 创建用户角色关系
        await UserRole.create(user=user, role=role)

        # 返回用户对象
        return user


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    role: Optional[str] = None   # 角色名字
    is_active: Optional[bool] = True
    password: Optional[str] = None
#用户更新
async def update_user_service(user_id: str, user_data: UserUpdate):
    async with in_transaction():
        # 查询用户 ORM 对象
        db_user = await User.filter(id=user_id).first()
        if not db_user:
            return None  # 或者 raise ValueError("用户不存在")

        # 更新基础信息（忽略 role, page, page_size）
        await User.filter(id=user_id).update(
            username=user_data.username,
            email=user_data.email,
            phone=user_data.phone,
            is_active=user_data.is_active
        )

        # 如果传了角色，更新绑定关系
        if user_data.role:
            # 查找角色
            role_db = await Role.get_or_none(role_name=user_data.role)
            if not role_db:
                raise ValueError(f"角色 {user_data.role} 不存在")

            # 更新关系表
            await UserRole.filter(user_id=user_id).update(role=role_db)

        # 重新查询更新后的用户对象返回
        updated_user = await User.filter(id=user_id).first()
        return updated_user



#用户删除`
async def delete_user_service(user_id: str):
    async with in_transaction():
        try:
            # 直接删除用户及其关联的角色关系
            deleted_count = await User.filter(id=user_id).delete()
            if deleted_count == 0:
                raise ValueError("用户不存在")
        except Exception as e:
            # 增加错误处理机制
            raise ValueError(f"删除用户时出错: {str(e)}")
    return None  # 返回 None 表示删除成功，或者可以选择返回 deleted_count 表示删除的记录数

