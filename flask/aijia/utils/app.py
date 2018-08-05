import os

import redis
from flask import Flask
from flask_session import Session

from user.models import db
from user.user_views import user_blueprint

se = Session()

def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    template_dir = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=template_dir)
    #注册视图路径
    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')


    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/aijia'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #模型建立需要初始化
    db.init_app(app=app)
    se.init_app(app=app)

    return app
