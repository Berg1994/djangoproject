from flask import Blueprint

# 初始化蓝图对象
stu_blueprint = Blueprint('stu', __name__)


@stu_blueprint.route('/')
def scores():
    return '分数'
