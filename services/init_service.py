import uuid
import asyncio
from tortoise import Tortoise
from models.user import User
from models.role import Role
from models.user_role import UserRole
from settings import TORTOISE_ORM, LOGGER_CONFIG
import logging.config

logging.config.dictConfig(LOGGER_CONFIG)
logger = logging.getLogger("init_service")


async def init_data():
    # 1. 初始化数据库连接
    await Tortoise.init(config=TORTOISE_ORM)

    # 2. 生成表（如果不存在）
    await Tortoise.generate_schemas()

    # 3. 插入数据
    user1 = await User.create(id=uuid.uuid4(), username="admin", password="admin",role="admin", email="")
    user2 = await User.create(id=uuid.uuid4(), username="engineer", password="123456", role="engineer", email="")
    user3 = await User.create(id=uuid.uuid4(), username="operator", password="123456",role="operator",  email="")

    role1 = await Role.create(id=uuid.uuid4(), role_name="admin", description="管理员")
    role2 = await Role.create(id=uuid.uuid4(), role_name="engineer", description="工程师")
    role3 = await Role.create(id=uuid.uuid4(), role_name="operator", description="操作员")

    # 外键关系：直接传对象，不用 .id
    await UserRole.create(id=uuid.uuid4(), user=user1, role=role1)
    await UserRole.create(id=uuid.uuid4(), user=user2, role=role2)
    await UserRole.create(id=uuid.uuid4(), user=user3, role=role3)

    logger.info("init data success")

    # 4. 关闭连接
    await Tortoise.close_connections()


if __name__ == "__main__":
    asyncio.run(init_data())
