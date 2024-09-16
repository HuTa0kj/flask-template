from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
lm = LoginManager()
# 配置 celery 启动配置
celery = Celery()
