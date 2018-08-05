from flask import render_template, Blueprint



blue = Blueprint('first', __name__)


@blue.route("/")
def hello():
    return "hello,world!"

#
# @blue.route("/hellohtml/")
# def hello_html():
#     return render_template('hello.html')
#
#
# # name 字符串 默认的   string:name
# @blue.route('/hello/<name>/')
# def hello_person(name):
#     return render_template('hello.html', name=name)
#
#
# @blue.route('/helloint/<int:id>/')
# def hello_int(id):
#     return render_template('hello.html', id=id)
#
#
# @blue.route('/hellofloat/<float:id>/')
# def hello_float(id):
#     return render_template('hello.html', id=id)
#
#
# @blue.route('/hellopath/<path:path>/')
# def hello_path(path):
#     return render_template('hello.html', path=path)
#
#
# @blue.route('/hellouuid/<uuid:uuid>/')
# def hello_uuid(uuid):
#     return render_template('hello.html', uuid=uuid)
