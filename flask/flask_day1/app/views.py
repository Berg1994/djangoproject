import uuid

from flask import Blueprint, request, make_response

app_buleprint = Blueprint('first', __name__)


# 构建路由
@app_buleprint.route('/')
# 找到url 后执行视图
def hello_world():
    return 'Hello World!'


@app_buleprint.route('/python')
def python():
    return '从入门到住院'


@app_buleprint.route('/postname', methods=['POST', 'GET'])
def post_name():
    return 'post请求'


@app_buleprint.route('/postname/<string:name>', methods=['POST', 'GET'])
def get_name(name):
    return '我是：%s' % name


@app_buleprint.route('/get_id/<int:id>', methods=['POST', 'GET'])
def get_num(id):
    print(type(id))
    return '数字：%d' % id


@app_buleprint.route('/get_fid/<float:fid>', methods=['POST', 'GET'])
def get_fid(fid):
    print(type(fid))
    return '数字：%.3f' % fid


@app_buleprint.route('/get_path/<path:path>')
def get_path(path):
    return '当前路径：%s' % path


@app_buleprint.route('/get_uuid')
def get_uuid():
    uid = uuid.uuid4()
    return '当前id：%s' % uid


@app_buleprint.route('/get_uu/<uuid:uid>')
def get_uu(uid):
    print(type(uid))
    return '当前id：%s' % uid


@app_buleprint.route('/get_response')
def get_response():
    res = make_response('<h2>我是响应</h2>')
    return res
