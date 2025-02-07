from flask_login import current_user

from app.database import UserTable


def get_current_uid(user_id):
    # 从 current_user.id 中获取 uid
    user = UserTable.query.filter_by(id=user_id).first()
    if user:
        return user.uid
    return None


def get_auth_user_id(token):
    """
    鉴权认证，支持登录状态或 API Key 的认证方式
    :param token: 用户的 API Key
    :return: (认证成功, 用户 UID)

    使用案例：
    api_key = request.headers.get("X-API-KEY")
    ok, user_uid = get_auth_user_id(api_key)
    if not ok:
        return jsonify({
            "code": 1,
            "msg": "无效的认证信息",
            "data": [],
        })
    all_tasks_info = Tasks.query.filter_by(user_uid=user_uid).all()
    """
    # 检查两种认证方式是否都不存在
    if not current_user.is_authenticated and not token:
        return False, None

    # 优先通过 API Key 认证
    if token:
        user_info = UserTable.query.filter_by(token=token).first()
        if user_info:
            return True, user_info.user_uid
        else:
            return False, None  # API Key 无效

    # 如果用户已登录，通过当前用户认证
    if current_user.is_authenticated:
        user_uid = get_current_uid(current_user.id)
        if user_uid:
            return True, user_uid
        else:
            return False, None  # 登录信息无效

    # 默认返回失败
    return False, None
