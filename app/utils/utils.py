import uuid
from werkzeug.security import generate_password_hash
from datetime import datetime


def get_date_time():
    """
    获取当前日期和时间
    :return:
    """
    current_datetime = datetime.now()
    # 格式化日期时间
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_datetime


def generate_hash_password(passwd):
    """
    PBKDF2 算法加密
    :param passwd: 原始明文密码
    :return:
    """
    new_passwd = generate_password_hash(passwd)
    return new_passwd


def generate_uuid():
    """
    使用 UUID4 生成一个 UUID
    :return: UUID
    """
    return str(uuid.uuid4())


def generate_user_token():
    """
    生成支持 API 调用的 Token
    :return:
    """
    return str(generate_uuid()).upper()
