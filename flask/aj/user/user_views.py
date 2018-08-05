import os
import random
import re

from flask import Blueprint, request, render_template, \
    url_for, redirect, jsonify, session

from user.models import db, User
from utils import status_code
from utils.functions import is_login
from utils.settings import upload_folder

user_blueprint = Blueprint('my_user', __name__)


@user_blueprint.route('/register/', methods=['GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')


@user_blueprint.route('/create_db/', methods=['GET'])
def create_db():
    db.create_all()
    return '创建成功'


@user_blueprint.route('/get_code/', methods=['GET'])
def get_code():
    code = ''
    s = '1234567890qwertyuiopasdfghjklzxcvbnm'
    for i in range(4):
        code += random.choice(s)
    # 往session 存值
    session['code'] = code
    return jsonify(code=200, msg='请求成功', data=code)


@user_blueprint.route('/register/', methods=['POST'])
def my_register():
    mobile = request.form.get('mobile')
    password = request.form.get('passwd')
    password2 = request.form.get('passwd2')
    imagecode = request.form.get('imagecode')

    # 验证参数是否完整
    if not all([mobile, password, password2, imagecode, ]):
        return jsonify(status_code.USER_REGISTER_PARAMS_VALID)

    # 验证图片验证码是否正确
    if session.get('code') != imagecode:
        return jsonify(status_code.USER_REGISTER_CODE_ERROR)

    # 验证手机号 ^1[3456789]\d{9}$
    if not re.match(r'^1[3456789]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_INVALID)

    # 判断密码
    if password != password2:
        return jsonify(status_code.USER_REGISTER_PASSWORD_ERROR)

    # 判断是否已经注册
    if User.query.filter(User.phone == mobile).count():
        return jsonify(status_code.USER_REGISTER_MOBILE_EXSIST)

    # 未注册
    user = User()
    user.phone = mobile
    user.password = password
    user.name = mobile

    try:
        user.add_update()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


# 注册
@user_blueprint.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


@user_blueprint.route('/login/', methods=['POST'])
def my_login():
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    if not all([mobile, password]):
        return jsonify(status_code.USER_LOGIN_PARAMS_INVALID)

    user = User.query.filter(User.phone == mobile).first()
    # 校验用户
    if user:
        if user.check_pwd(password):
            # 密码校验成功
            session['user_id'] = user.id
            return jsonify(status_code.SUCCESS)
        else:
            return jsonify(status_code.USER_LOGIN_PARMAS_VALID)

    else:
        return jsonify(status_code.USER_LOGIN_PHTON_INVALID)


@user_blueprint.route('/logout/', methods=['GET'])
@is_login
def logout():
    session.clear()
    return jsonify(status_code.SUCCESS)


@user_blueprint.route('/my/', methods=['GET'])
@is_login
def my():
    return render_template('my.html')



# 获取用户信息
@user_blueprint.route('/userinfo/', methods=['GET'])
def user_info():
    user_id = session['user_id']
    user = User.query.get(user_id)
    user_info = user.to_basic_dict()
    return jsonify(user_info=user_info, code=status_code.OK)


@user_blueprint.route('/profile/', methods=['GET'])
def profile():
    user = User.query.filter(User.id == session['user_id']).first()
    return render_template('profile.html', user=user)


@user_blueprint.route('/profile/', methods=['PATCH'])
def my_profile():
    # 修改用户名
    username = request.form.get('name')
    if username:
        if User.query.filter(User.name == username).count():
            return jsonify(status_code.USER_USERINFO_NAME_EXSIST)

        user = User.query.get(session['user_id'])
        user.name = username
        user.add_update()


    # 修改头像
    avatar = request.files.get('avatar')
    if avatar:
        # 验证图片 mimetype = 'image/jpeg' png
        if not re.match(r'image/*', avatar.mimetype):
            return jsonify(status_code.USER_USERINOF_PORFILE_AVATAR_INVALID)

        # 图片保存  media/uplode/xxx.jpg
        avatar.save(os.path.join(upload_folder, avatar.filename))
        # 修改用户的avatar字段
        user = User.query.get(session['user_id'])
        avatar_addr = os.path.join('upload', avatar.filename)
        user.avatar = avatar_addr
        try:
            user.add_update()
            return jsonify(code=status_code.OK, avatar=avatar_addr)
        except Exception as e:
            print(e)
            return jsonify(status_code.DATABASE_ERROR)
    return jsonify(status_code.OK)

        # if not all([username, avatar]):
        #     return jsonify(status_code.USER_SET_PARAMS_INVALID)
        #
        # user = User.query.filter(User.id == session['user_id']).first()
        # user.name = username
        # user.avatar = avatar


@user_blueprint.route('/auth/', methods=['GET'])
def auth():
    return render_template('auth.html')


@user_blueprint.route('/auth/', methods=['PATCH'])
def my_auth():
    real_name = request.form.get('real_name')
    id_card = request.form.get('id_card')

    if not all([real_name, id_card]):
        return jsonify(status_code.USER_USERINFO_ID_NAME_CARD_INVALID)
    if not re.match(r'[1-9]\d{16}[0-9X]', id_card):
        return jsonify(status_code.USER_USERINFO_IDCARD_INVALID)

    user = User.query.get(session['user_id'])
    user.id_name = real_name
    user.id_card = id_card

    try:
        user.add_update()
        return jsonify(code=status_code.OK)

    except Exception as e:
        print(e)
        return jsonify(status_code.DATABASE_ERROR)


@user_blueprint.route('/real_user_info/', methods=['GET'])
def real_user_info():
    user = User.query.get(session['user_id'])
    user = user.to_auth_dict()
    return jsonify(code=status_code.OK, user=user)

