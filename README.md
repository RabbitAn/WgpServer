# WgpServer

WgpServer 是一个基于 FastAPI 的后端服务项目，提供了用户管理、角色管理和身份验证等功能。

## 项目结构

```
WgpServer/
├── migrations/          # 数据库迁移文件
├── models/              # 数据模型定义
├── routers/             # API路由
├── services/            # 业务逻辑层
├── main.py             # 应用入口文件
├── settings.py         # 配置文件
└── README.md           # 项目说明文档
```

## 功能特性

- 用户管理：支持用户的增删改查操作
- 角色管理：支持角色的分配和管理
- 身份验证：基于 JWT 的用户认证和授权机制
- 日志记录：多级别日志记录系统
- 数据库：使用 PostgreSQL 作为数据存储

## 技术栈

- [FastAPI](https://fastapi.tiangolo.com/) - 现代、快速（高性能）的 Python Web 框架
- [Tortoise ORM](https://tortoise-orm.com/) - 易于使用的异步 Python ORM
- [PostgreSQL](https://www.postgresql.org/) - 强大的开源关系数据库
- [JWT](https://jwt.io/) - JSON Web Tokens 实现安全认证
- [Uvicorn](https://www.uvicorn.org/) - 快速的 ASGI 服务器

## 配置要求

在运行项目之前，请确保已安装以下依赖：

- Python 3.8+
- PostgreSQL 数据库
- 相关 Python 包（见 `pyproject.toml`）

## 安装步骤

1. 克隆项目到本地：
   ```bash
   git clone <repository-url>
   cd WgpServer
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
   
   或者使用 Poetry（如果项目使用 Poetry 管理依赖）：
   ```bash
   poetry install
   ```

3. 配置数据库：
   在 `settings.py` 中修改数据库连接配置：
   ```python
   TORTOISE_ORM = {
       "connections": {
           "default": {
               "engine": "tortoise.backends.asyncpg",
               "credentials": {
                   "host": "localhost",
                   "port": 5432,
                   "user": "your_username",
                   "password": "your_password",
                   "database": "your_database"
               }
           }
       },
       # ... 其他配置
   }
   ```

4. 运行应用：
   ```bash
   python main.py
   ```
   
   或使用 Uvicorn：
   ```bash
   uvicorn main:app --reload
   ```

## API 接口

启动服务后，可以通过以下地址访问 API：

- 主服务地址：http://127.0.0.1:8080
- API 文档：http://127.0.0.1:8080/docs
- ReDoc 文档：http://127.0.0.1:8080/redoc

主要接口包括：
- `/user` - 用户管理相关接口
- `/role` - 角色管理相关接口
- `/login` - 用户登录接口

## 认证机制

本项目使用 JWT（JSON Web Token）进行身份验证：

1. 用户通过 `/login` 接口登录获取 access_token
2. 在需要认证的接口请求中，在 Header 中添加：
   ```
   Authorization: Bearer <your_token>
   ```

## 日志系统

项目包含完善的日志记录功能，日志按级别分类存储：

- INFO 级别日志存储在 `logs/info/` 目录下
- WARNING 级别日志存储在 `logs/warning/` 目录下
- ERROR 级别日志存储在 `logs/error/` 目录下

## 开发规范

- 使用 Tortoise ORM 进行数据库操作
- 所有业务逻辑应放在 `services/` 目录下
- API 路由定义在 `routers/` 目录下
- 数据模型定义在 `models/` 目录下

## 注意事项

1. 请勿将真实的数据库密码等敏感信息提交到代码仓库
2. 生产环境部署时，请修改 `settings.py` 中的 SECRET_KEY
3. 建议定期备份数据库以防止数据丢失

## 许可证

本项目仅供学习和参考使用。