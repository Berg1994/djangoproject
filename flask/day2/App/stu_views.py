from flask import Blueprint, render_template, request, session, make_response

from App.models import db, Student

stu_blueprint = Blueprint('stu', __name__)

"""
分数
"""


@stu_blueprint.route('/scores/', methods=['GET'])
def stu_scores():
    scores = [90, 80, 76, 56, 59]
    content_h2 = '<h2>二班海飞丝最美</h2>'
    return render_template('scores.html',
                           scores=scores,
                           content_h2=content_h2)


"""
创建学生表
"""


@stu_blueprint.route('/create_db_stu/')
def create_db_stu():
    db.create_all()
    return '创建成功'


"""
删除学生表
"""


@stu_blueprint.route('/drop_db_stu/')
def drop_db_stu():
    db.drop_all()
    return '删除成功'


"""
创建学生
"""


@stu_blueprint.route('/create_stu/', methods=['GET'])
def create_stu():
    stu = Student()
    stu.s_name = '张三'
    stu.s_age = '17'
    db.session.add(stu)
    db.session.commit()

    return '创建学生成功'


"""
查询学生
"""


@stu_blueprint.route('/select_stu/', methods=['GET'])
def select_stu():
    # stus = Student.query.filter(Student.s_name == '张三')
    # stus = Student.query.filter_by(s_name='张三')
    # stus = Student.query.all()
    stu = Student.query.filter(Student.s_name == '张三').first()
    stu.s_name = '李四'
    db.session.add(stu)
    db.session.commit()

    # return render_template('students.html', stus=stus)
    return '查询成功'


"""
学生登录
"""


@stu_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        session['username'] = username
        return render_template('login.html', username=username)


"""
设置COOKIE
"""


@stu_blueprint.route('/setcookie/')
def set_cookie():
    temp = render_template('cookies.html')
    # 服务端创建响应
    res = make_response(temp)
    # 绑定cookie值, set_cookie(key,value,max_age, expires)
    res.set_cookie('ticket', '123123123', max_age=10)

    return res


"""

删除COOKIE
"""


@stu_blueprint.route('/delcookie/')
def del_cookie():
    tmep = render_template('cookies.html')
    res = make_response(tmep)
    res.delete_cookie('ticket')
    return res
