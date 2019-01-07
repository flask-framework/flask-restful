import os
import redis
from datetime import timedelta

# 安装的应用
INSTALL_APPS = [

]

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = b"\x15\xb8\xa1\xc8\xcb\xf7;\xee\xb46\xc9\xaep\xadld\x8dM\xc6\xc9SV\xefO"

# SQLALCHEMY数据库配置
SQLALCHEMY_DATABASE_URI = ""
SQLALCHEMY_ECHO = False
SQLALCHEMY_POOL_SIZE = 200
SQLALCHEMY_TRACK_MODIFICATIONS = True

# SESSION
SESSION_COOKIE_NAME = ""
SESSION_TYPE = "redis"
SESSION_REDIS = redis.Redis(host="127.0.0.1", port=6379, db=5)
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

# 文件上传配置
UPLOADED_FILES_DEST = os.path.join(BASE_DIR, "static/upload")
UPLOADED_FILES_URL = "/media"
UPLOADED_FILES_ALLOW = ""
UPLOADED_FILES_DENY = ""

# 国际化配置
BABEL_DEFAULT_LOCALE = "zh_Hans_CN"
BABEL_DEFAULT_TIMEZONE = "Asia/Shanghai"

# 分页大小
PAGE_SIZE = 20

# JWT认证配置
JWT_EXPIRED = timedelta(days=3)     # 过期时间
JWT_MODEL = ""      # 认证model类
