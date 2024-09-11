import base64
from flask import current_app, abort
from itsdangerous import URLSafeTimedSerializer

'''
常用的封装函数
'''


def encry_auth(user_email):
    serializer = URLSafeTimedSerializer(current_app.secret_key)
    auth = serializer.dumps({'user_email': user_email})
    return auth


def decry_auth(auth):
    serializer = URLSafeTimedSerializer(current_app.secret_key)
    # 解密错误，显示401
    try:
        user_email = serializer.loads(auth)['user_email']
    except:
        abort(401)
    return user_email


def bs4_en(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')


def bs4_de(text):
    return base64.b64decode(text.encode('utf-8')).decode('utf-8')
