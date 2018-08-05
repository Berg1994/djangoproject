from flask import Blueprint, render_template, make_response, request, session, redirect, url_for
from App.models import db, UserModel
from werkzeug.security import generate_password_hash, check_password_hash

user_blueprint = Blueprint('user', __name__)

"""
创建用户表
"""


@user_blueprint.route('/create_db_user/')
def create_db_user():
    db.create_all()
    return '创建成功'


"""

注册用户
"""


@user_blueprint.route('/register_user/', methods=['GET', 'POST'])
def register_user():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        user = UserModel()
        user.username = request.form.get('username')
        user.email = request.form.get('email')
        user.password = request.form.get('password')
        # user.user_id = request.form.get('user_id')
        if len(user.username) == 0 or len(user.email) == 0 or len(user.password) == 0:
            context = '请填写完整'
            return render_template('register.html', context=context)
        else:
            user.password = generate_password_hash(user.password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login_user'))


"""
登录用户

"""


@user_blueprint.route('/login_user/', methods=['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = UserModel.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password,password):
                return redirect(url_for('stu.stu_scores'))
            context = '用户名或者密码错误'
            return render_template('login.html',context=context)
        context = '用户名或者密码错误'
        return render_template('login.html',context=context)


@user_blueprint.route('/logout_user/', methods=['GET'])
def logout():
    return redirect(url_for('user.login_user'))
