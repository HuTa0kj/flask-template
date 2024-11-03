from app.read_config import read_config


class BaseConfig(object):
    config_info = read_config()
    DEBUG = False
    SECRET_KEY = 'xxx'
    HOSTNAME = config_info['SET']['DATABASE']['MYSQL']['HOSTNAME']
    PORT = config_info['SET']['DATABASE']['MYSQL']['PORT']
    USERNAME = config_info['SET']['DATABASE']['MYSQL']['USERNAME']
    PASSWORD = config_info['SET']['DATABASE']['MYSQL']['PASSWORD']
    DATABASE = config_info['SET']['DATABASE']['MYSQL']['DATABASE']
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

    REDIS_HOST = config_info['SET']['DATABASE']['REDIS']['HOST']
    BROKER_ID = config_info['SET']['DATABASE']['REDIS']['BROKER_ID']
    BACKEND_ID = config_info['SET']['DATABASE']['REDIS']['BACKEND_ID']
    CELERY_BROKER_URL = f'redis://{REDIS_HOST}:6379/{BROKER_ID}'
    CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:6379/{BACKEND_ID}'

    broker_connection_retry_on_startup = True

    # celery 定时任务配置
    CELERY_BEAT_SCHEDULE = {
        'log-access-time-every-minute': {
            'task': 'app.tasks.log_access_schedule_time',
            'schedule': 60.0,  # 每60秒执行一次
        },
    }


class DevConfig(BaseConfig):
    DEBUG = True
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False
