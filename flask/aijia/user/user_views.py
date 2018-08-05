import os
import re

from flask import Blueprint, render_template, redirect, url_for, session, request, jsonify

from user.models import db, User
from utils import status_code
from utils.functions import is_login
from utils.setting import UPLOAD_DIR

user_blueprint = Blueprint('user', __name__)


# 第一个视图
@user_blueprint.route('/')
def hello():
    return 'hello,world!'


# 创建数据库
@user_blueprint.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'


@user_blueprint.route('/register/', methods=['GET'])
def register():
    return render_template('register.html')


@user_blueprint.route('/register/', methods=['POST'])
def user_regiter():
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if not all([mobile, password, password2]):
        return jsonify(status_code.USER_REGISTER_DATA_NOT_NULL)
    if not re.match(r'^1[3456789]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_ERROR)
    if password != password2:
        return jsonify(status_code.USER_REGISTER_PASSWORD_IS_NOT_VALID)

    user = User.query.filter(User.phone == mobile).all()
    if user:
        return jsonify(status_code.USER_REGISTER_MOBILE_EXSITS)
    else:
        user = User()
        user.phone = mobile
        user.password = password
        user.name = mobile
        try:
            user.add_update()
        except Exception as e:
            db.session.rollback()
            return jsonify(status_code.DATABASE_ERROR)
        return jsonify(status_code.SUCCESS)


@user_blueprint.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


@user_blueprint.route('/login/', methods=['POST'])
def user_login():
    mobile = request.form.get('mobile')
    password = request.form.get('password')

    if not all([mobile, password]):
        return jsonify(status_code.USER_REGISTER_DATA_NOT_NULL)
    if not re.match(r'^1[34578]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_ERROR)
    user = User.query.filter(User.phone == mobile).first()
    if user:
        if not user.check_pwd(password):
            return jsonify(status_code.USER_REGISTER_PASSWORD_IS_NOT_VALID)
        session['user_id'] = user.id
        return jsonify(status_code.SUCCESS)
    else:
        return jsonify(status_code.USER_REGISTER_MOBILE_ERROR)


@user_blueprint.route('/my/', methods=['GET'])
def my():
    return render_template('my.html')


@user_blueprint.route('profile', methods=['GET'])
def profile():
    return render_template('profile.html')


@user_blueprint.route('/profile/', methods=['PATCH'])
def user_profile():
    file = request.files.get('avatar')

    # 校验上传图片格式的正确性
    if not re.match(r'image/.*', file.mimetype):
        return jsonify(status_code.USER_CHANGE_PROFILE_IMAGES)

    image_path = os.path.join(UPLOAD_DIR, file.filename)
    file.save(image_path)

    user = User.query.get(session['user_id'])
    avatar_path = os.path.join('upload', file.filename)

    user.avatar = avatar_path

    try:
        user.add_update()

    except Exception as e:
        db.session.rollback()
        return jsonify(status_code.DATABASE_ERROR)
    return jsonify(code=status_code.OK, image_url=avatar_path)

@user_blueprint.route('/proname/',methods=['PATCH'])
@is_login
def user_proname():
    name = request.form.get('name')
    user = User.query.filter(User.name == name).first()

    if user:
        #过滤用户民是否存在
        return jsonify(status_code.USER_CHANGE_PRONAME_IS_INVALID)
    else:
        user = User.query.get(session['user_id'])
        user.name = name
        try:
            user.add_update()
        except:
            db.session.rollback()
            return jsonify(status_code.DATABASE_ERROR)
        return jsonify(code=status_code.OK, name=name)


@user_blueprint.route('/user/', methods=['GET'])
@is_login
def user_info():
    user = User.query.get(session['user_id'])
    return jsonify(code=status_code.OK, user_info=user.to_basic_dict())

@user_blueprint.route('auth', methods=['GET'])
def auth():
    return render_template('auth.html')

@user_blueprint.route('auth',methods=['PATCH'])
def user_auth():
    pass
