from flask import Blueprint, jsonify, request

from app.database import UserTable
from app.utils.auth import get_auth_user_id

user_info_select_api = Blueprint('user_info_select_api', __name__, url_prefix="/api")


# 查询当前用户的任务列表
@user_info_select_api.route('/user/info', methods=['GET'])
def get_user_name():
    api_key = request.headers.get("X-API-KEY")
    ok, user_uid = get_auth_user_id(api_key)
    if not ok:
        return jsonify({
            "code": 1,
            "msg": "无效的认证信息",
            "data": [],
        })
    user_info = UserTable.query.filter_by(user_uid=user_uid).first()
    if not user_info:
        return jsonify({
            "code": 1,
            "msg": "无相关用户",
            "data": [],
        })
    return jsonify({
        "code": 0,
        "msg": "查询成功",
        "data": {
            "uid": user_info.user_uid,
            "username": user_info.username,
        },
    })
