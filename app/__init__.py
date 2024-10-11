from flask import Flask
from app.views.user.user import user
from app.models import LoginUser
from app.extensions import lm, db, celery
from app.config import BaseConfig


def create_app(config=BaseConfig):
    app = Flask(__name__)
    # 注册蓝图
    app.config.from_object(config)

    # 注册扩展（包括Celery）
    register_extensions(app)

    # 注册蓝图
    register_blueprints(app)

    celery = make_celery(app)
    celery.set_default()

    return app, celery


# 插件注册
def register_extensions(app):
    lm.init_app(app)
    # 设置登录端点
    lm.login_view = 'user.login'
    db.init_app(app)


# 初始化 Celery
def make_celery(app):
    # 使用Flask应用的配置初始化Celery
    celery.conf.update(
        broker_url=app.config["CELERY_BROKER_URL"],
        result_backend=app.config["CELERY_RESULT_BACKEND"],
        beat_schedule=app.config["CELERY_BEAT_SCHEDULE"]
    )

    # 自动发现任务
    celery.autodiscover_tasks(['app.tasks'])

    class ContextTask(celery.Task):
        """为 Celery 任务提供 Flask 应用上下文"""

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    # 设置 Celery 使用应用上下文任务
    celery.Task = ContextTask
    return celery


# 蓝图注册
def register_blueprints(app):
    app.register_blueprint(user)


@lm.user_loader
def load_user(user_id):
    user = LoginUser(user_id)
    return user
