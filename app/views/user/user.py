from werkzeug.security import check_password_hash
from flask import Blueprint, request, redirect, render_template, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from celery.result import AsyncResult
from app.tasks import log_access_time
from app.database import UserTable
from app.models import LoginUser
from app.utils.log import logger

user = Blueprint('user', __name__)


# 登录
@user.route('/', methods=['GET', 'POST'])
@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        username = request.form.get('username')  # 传入表单对应输入字段的 name 值
        password = request.form.get('password')
        users = UserTable.query.filter_by(username=username).first()

        if not users:
            return jsonify({'status': 'User not found'}), 404

        if check_password_hash(users.password, password):
            # 设置用户登录
            login_user(LoginUser(users.id))
            logger.info(f"用户：{username} 登录成功")

            # 调用 Celery 任务，延迟执行
            task = log_access_time.delay(current_user.id)

            return jsonify({
                'task_id': task.id,  # 返回任务ID
                'status': 'Login successful'
            })
        else:
            return jsonify({'status': 'Invalid password'}), 400


# 查询任务状态
@user.route('/task_status', methods=['GET'])
@login_required
def get_task_status():
    task_id = request.args.get('task_id')
    if not task_id:
        return jsonify({'status': 'Task not found'}), 404
    task = AsyncResult(task_id)  # 查询任务结果
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Pending...',
        }
    elif task.state == 'SUCCESS':
        response = {
            'state': task.state,
            'result': task.result,  # 返回任务的执行结果
        }
    else:
        response = {
            'state': task.state,
            'status': str(task.info),  # 若任务失败，返回异常信息
        }
    return jsonify(response)


@user.route('/dashboard')
@login_required
def dashboard():
    # 获取当前用户信息
    user_id = current_user.id
    user = UserTable.query.get(user_id)
    return f"欢迎 {user.username} 到你的仪表盘！"


# 注销
@user.route('/login_out')
@login_required
def login_out():
    logout_user()
    # 刷新页面的时候，做重定向，不要直接修改
    response = redirect('/')
    return response
