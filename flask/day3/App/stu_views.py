import random

from flask import Blueprint, render_template, request, redirect, url_for

from App.models import db, Student

stu_blueprint = Blueprint('stu', __name__)

"""
创建库
"""


@stu_blueprint.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'


"""
删除库
"""


@stu_blueprint.route('/drop_db/')
def drop_db():
    db.drop_all()
    return '删除成功'


"""
学生列表显示
"""


@stu_blueprint.route('/stu_list/')
def stu_list():
    stus = Student.query.all()
    # 使用sql
    # sql = 'select * from student'
    # stus = db.session.execute(sql)
    return render_template('students.html', stus=stus)


"""
创建学生
"""


@stu_blueprint.route('/create_stu/', methods=['GET', 'POST'])
def create_stu():
    if request.method == 'GET':
        return render_template('create_student.html')

    if request.method == 'POST':
        username = request.form.get('username')
        stu = Student()
        stu.s_name = username

        db.session.add(stu)
        db.session.commit()

        return '创建%s学生成功' % username


"""

批量创建学生
"""


@stu_blueprint.route('/create_stus/', methods=['GET'])
def create_stus():
    stu_list = []

    for _ in range(10):
        stu = Student()
        stu.s_name = '温婉%s' % random.randrange(1000)
        stu.s_age = '%s' % random.randrange(20)
        stu_list.append(stu)

    db.session.add_all(stu_list)
    db.session.commit()

    return '妹纸创建成功'


"""
编辑学生
"""


@stu_blueprint.route('/update_stu/', methods=['GET', 'POST'])
def update_stu():
    if request.method == 'GET':
        id = request.args.get('id')
        stu = Student.query.filter(Student.s_id == id).first()
        return render_template('stu_edit.html', stu=stu)

    if request.method == 'POST':
        s_id = request.form.get('s_id')
        s_name = request.form.get('username')
        s_age = request.form.get('age')

        stu = Student.query.filter_by(s_id=s_id).first()
        stu.s_name = s_name
        stu.s_age = s_age
        # 修改，add操作可有可没有
        db.session.add(stu)
        db.session.commit()

        return redirect(url_for('stu.stu_list'))


"""
不同方式查询学生 根据ID 查询 年龄 结尾 限制显示 
"""


@stu_blueprint.route('/stu_in/', methods=['GET'])
def stu_in_ids():
    # stus = Student.query.filter(Student.s_id.in_([3, 4, 5, 6, 7]))
    # stus = Student.query.filter(Student.s_age.__lt__(19))
    # stus = Student.query.filter(Student.s_name.endswith('9'))
    # stus = Student.query.filter(Student.s_name.like('%温%'))
    # stus = Student.query.order_by('s_id').offset(3)
    # stus = Student.query.order_by('s_id').offset(3).limit(5)
    stus = Student.query.paginate(3, 10)
    paginate = stus.items
    return render_template('students.html', stus=stus)


"""
分页
"""


@stu_blueprint.route('/paginate/', methods=['GET'])
def stu_paginate():
    if request.method == 'GET':
        page = int(request.args.get('page', 1))
        page_num = 10
        paginate = Student.query.order_by('s_id').paginate(page, page_num)
        stus = paginate.items

        return render_template('stu_paginate.html', stus=stus, paginate=paginate)


