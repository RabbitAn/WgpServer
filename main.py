from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from fastapi.security import OAuth2PasswordBearer
from settings import TORTOISE_ORM,LOGGER_CONFIG
from routers.index import api_router
import uvicorn
import logging.config
from settings import LOGGER_CONFIG

logging.config.dictConfig(LOGGER_CONFIG)
logger = logging.getLogger(__name__)

app = FastAPI()

# 允许跨域的来源
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:8080",
    # 还可以加其他域名
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # 允许的来源
    allow_credentials=True,       # 是否允许Cookie
    allow_methods=["*"],           # 允许所有方法，包括OPTIONS
    allow_headers=["*"],           # 允许所有请求头
)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
async def root():
    logger.info("Hello World")
    return {"message": "Hello World"}
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)