from flask import Flask

from app.views.user.user import user
from app.views.admin.admin import admin
from app.models import LoginUser
from app.extensions import lm, db
from app.config import BaseConfig


def create_app(config=BaseConfig):
    app = Flask(__name__)
    # 注册蓝图
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)

    return app


# 插件注册
def register_extensions(app):
    lm.init_app(app)
    lm.login_view = 'user.login'
    db.init_app(app)


# 蓝图注册
def register_blueprints(app):
    app.register_blueprint(user)
    app.register_blueprint(admin)


@lm.user_loader
def load_user(user_id):
    user = LoginUser(user_id)
    return user
