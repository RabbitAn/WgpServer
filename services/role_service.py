from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel
from models.role import Role

class RoleIn(BaseModel):
    role_name: Optional[str] = None
    page:int = 1
    page_size:int = 10

class RoleOut(BaseModel):
    id: str
    role_name: str
    description: Optional[str] = None
    created_at: datetime
    updated_at:datetime

# ---- Service Functions ----
# 查询角色
async def query_role_service(input: RoleIn):
    query = Role.all()
    if input.role_name:
        query = query.filter(role_name=input.role_name)
    roles = await query
    res=[]
    for role in roles:
        role_out = RoleOut(
            id=str(role.id),
            role_name=role.role_name,
            description=role.description,
            created_at=role.created_at,
            updated_at=role.updated_at
        )
        res.append(role_out)
    return {"roles":res,"total":len(roles),"page":input.page,"page_size":input.page_size}

# 创建角色
async def create_role_service(input: RoleIn) :
    role = await Role.create(
        role_name=input.role_name,
        description=input.description
    )
    role_out = RoleOut(
        id=str(role.id),
        role_name=role.role_name,
        description=role.description,
        created_at=role.created_at,
        updated_at=role.updated_at
    )
    return role_out

# 更新角色
async def update_role_service(id: str, input: RoleIn) :
    role = await Role.get_or_none(id=id)
    if not role:
        return None  # 或抛异常
    if input.role_name:
        role.role_name=input.role_name
    if input.description:
        role.description=input.description
    role.description=input.description
    await role.save()
    role_out = RoleOut(
        id=str(role.id),
        role_name=role.role_name,
        description=role.description,
        created_at=role.created_at,
        updated_at=role.updated_at)
    return role_out

# 删除角色
async def delete_role_service(id: str):
    role = await Role.get_or_none(id=id)
    if not role:
        return False  # 或抛异常
    await role.delete()
    return True
