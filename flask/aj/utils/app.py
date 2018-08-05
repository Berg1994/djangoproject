

import redis
from flask_session import Session

from flask import Flask


from user.models import db
from user.order_views import order_blueprint
from user.user_views import user_blueprint
from user.house_views import house_blueprint
from utils.functions import get_sqlalchemy_uri
from utils.settings import static_dir, template_dir, MYSQL_DATABASE, REDIS_DATABASE
# from flask_debugtoolbar import DebugToolbarExtension


def create_app():
    # 写法一  目的获取模板和静态资源路径
    # app = Flask(__name__,
    #             static_folder='../static',
    #             template_folder='../tempaltes')

    # 写法二
    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=template_dir, )
    # 注册蓝图
    app.register_blueprint(user_blueprint, url_prefix='/my_user')
    app.register_blueprint(house_blueprint, url_prefix='/house')
    app.register_blueprint(order_blueprint, url_prefix='/order')


    # 设置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = get_sqlalchemy_uri(MYSQL_DATABASE)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = redis.Redis(host=REDIS_DATABASE['HOST'],
                                              port=REDIS_DATABASE['PORT'])

    app.config['SECRET_KEY'] = '123456'
    app.debug = True

    # bar = DebugToolbarExtension()
    se = Session()

    # bar.init_app(app)
    se.init_app(app)
    db.init_app(app)

    return app
