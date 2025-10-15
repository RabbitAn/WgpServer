import os
import logging
import logging.config



# 根目录 logs 路径
BASE_LOG_PATH = os.path.join(os.path.dirname(__file__), "logs")

LOG_DIRS = {
    "info": os.path.join(BASE_LOG_PATH, "info"),
    "warning": os.path.join(BASE_LOG_PATH, "warning"),
    "error": os.path.join(BASE_LOG_PATH, "error"),
}

# 确保文件夹存在
for path in LOG_DIRS.values():
    os.makedirs(path, exist_ok=True)

LOGGER_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(filename)s[line:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        # 控制台输出
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout',
            'level': 'DEBUG'
        },
        # Info 按天生成
        'info_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOG_DIRS["info"], "info.log"),
            'when': 'midnight',   # 每天滚动
            'backupCount': 30,    # 保留30天
            'encoding': 'utf-8',
            'level': 'INFO'
        },
        # Warning 按天生成
        'warning_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOG_DIRS["warning"], "warning.log"),
            'when': 'midnight',
            'backupCount': 30,
            'encoding': 'utf-8',
            'level': 'WARNING'
        },
        # Error 按天生成
        'error_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOG_DIRS["error"], "error.log"),
            'when': 'midnight',
            'backupCount': 30,
            'encoding': 'utf-8',
            'level': 'ERROR'
        },
    },
'loggers': {
        'tortoise': {  # Tortoise ORM 的主 logger
            'level': 'WARNING',
            'handlers': ['console'],  # 可以只留控制台
            'propagate': False
        },
        'tortoise.backends.asyncpg': {  # 子 logger
            'level': 'WARNING',
            'handlers': ['console'],
            'propagate': False
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'info_file', 'warning_file', 'error_file']
    }
}



TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "localhost",
                "port": 5432,
                "user": "postgres",
                "password": "123456",
                "database": "fastapi_server"
            }
        }
    },
    "apps": {
        "models": {
            "models": [
                "models.user",
                "models.role",
                "models.user_role",
                "aerich.models"
            ],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai",
    "generate_schemas": True,
}


SECRET_KEY = "your_secret_key_here_to_encrypt_the_access_token"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 12*60 #最小有效期0.5天



