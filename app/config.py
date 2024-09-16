class BaseConfig(object):
    SECRET_KEY = 'xxx'
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    USERNAME = 'root'
    PASSWORD = '123456'
    DATABASE = 'web_scan'
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"


class DevConfig(BaseConfig):
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False
