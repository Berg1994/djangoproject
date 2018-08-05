import os

import redis
from flask import Flask

from App.stu_views import stu_blueprint
from App.user_views import user_blueprint
from utils.exts__init import ext_init


def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=templates_dir)

    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
    app.register_blueprint(blueprint=stu_blueprint, url_prefix='/stu')

    app.debug = True

    secret_key = os.urandom(16)
    app.config['SECRET_KEY'] = secret_key
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/hello_flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    ext_init(app)

    return app
