class BaseConfig(object):
    SECRET_KEY = 'xxx'
    HOSTNAME = 'mysql'
    PORT = '3306'
    USERNAME = 'root'
    PASSWORD = '123456'
    DATABASE = 'flask_app'
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

    REDIS_HOST = 'redis'
    CELERY_BROKER_URL = f'redis://{REDIS_HOST}:6379/1',
    CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:6379/2'


class DevConfig(BaseConfig):
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False
