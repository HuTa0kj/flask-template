from flask import Blueprint, render_template, request, redirect
from flask_login import login_required

from app.views.common import decry_auth

admin = Blueprint('administrator', __name__)


@admin.route('/')
@admin.route('/index/')
@login_required
def index():
    auth = request.cookies.get('auth')
    email = decry_auth(auth)
    return render_template('admin/index.html', email=email, isactive='home')


@admin.route('/add_site/', methods=['GET', 'POST'])
@login_required
def add_site():
    auth = request.cookies.get('auth')
    email = decry_auth(auth)
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        target = request.form.get('target')
        remark = request.form.get('remark')
        print(target)
        print(remark)
        # 接收到参数后返回一个弹窗，并重定向到 index
        if target and remark:
            response = redirect('/index/')
            return response
    return render_template('admin/add_site.html', email=email, isactive='add_site')


@admin.route('/vul_scan/', methods=['GET', 'POST'])
@login_required
def vul_scan():
    auth = request.cookies.get('auth')
    email = decry_auth(auth)
    return render_template('admin/vul_scan.html', email=email, isactive='vul_scan')
