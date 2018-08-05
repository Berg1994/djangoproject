import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from flask_script import Manager

from flask_session import Session

from app import api
from app.views import app_blueprint

from app.models import db

BASE_DIR = os.path.dirname(__file__)
# print(BASE_DIR)

template_dir = os.path.join(BASE_DIR, 'templates')
# print(template_dir)

app = Flask(__name__,
            template_folder=template_dir)

# 第一种
se = Session()

# db.session.commit()
# 第二种
# Session(app=app)

# 将模型和app对象绑定


# prefix url前缀
app.register_blueprint(app_blueprint, url_prefix='/app')

# app.config['SESSION_TYPE'] = 'redis'
# # 访问redis
# app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
# session的实例需要获取数据库的配置
se.init_app(app)
# 定义前缀
# app.config['SESSION_KEY_PREFIX'] = 'flask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'SECRET_KEY'

# 因为db初始化需要读取上面2个配置 所以必须写在两个配置后面
db.init_app(app)

app.debug = True

debug = DebugToolbarExtension()
debug.init_app(app)

api.init_app(app)

manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()
