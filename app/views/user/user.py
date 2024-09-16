from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, login_user, logout_user

from app.views.common import encry_auth
from app.database import UserTable
from app.models import LoginUser

user = Blueprint('user', __name__)


# 登录
@user.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        email = request.form.get('email')  # 传入表单对应输入字段的 name 值
        password = request.form.get('password')
        users = UserTable.query.filter_by(email=email).first()
        if users:
            if users.password == password:
                print(users.email)
                print(users.password)
                # 设置用户登录
                login_user(LoginUser(users.id))
                # 用户信息存储在auth字段
                auth = encry_auth(email)
                response = redirect('/index/')
                response.set_cookie('auth', auth)
                return response
            else:
                return redirect('/login/')
        else:
            return redirect('/login/')
    return render_template('user/login.html')


# 注销
@user.route('/login_out/')
@login_required
def login_out():
    logout_user()
    # 刷新页面的时候，做重定向，不要直接修改
    response = redirect('/')
    return response


@user.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('404.html'), 404  # 返回模板和状态码
