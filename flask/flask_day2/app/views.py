import random

from datetime import datetime

from flask import Blueprint, redirect, url_for, abort, request, render_template, session
from sqlalchemy import and_, or_, not_

from app.models import db, Student, Grade, Course
from utils.functions import is_login

from app import api
from flask_restful import Resource


app_blueprint = Blueprint('first', __name__)


@app_blueprint.route('/')
def hello():
    return 'hello'


@app_blueprint.route('/getredirect/')
def get_redirect():
    #
    # return redirect('/app/')
    # url_for('初始化蓝图的第一个参数，函数名')
    return redirect(url_for('first.hello'))


@app_blueprint.route('/geterror/')
def get_error():
    try:
        3 / 0
    except Exception as e:
        abort(400)

    return '计算'


@app_blueprint.errorhandler(400)
def handler(exception):
    return '捕获异常： %s' % exception


@app_blueprint.route('/logins/')
def logins():
    if request.method == 'GET':
        username = session.get('username')
        return render_template('login_s.html', username=username)

    if request.method == 'POST':
        username = request.form.get('username')
        session['username'] = username
        return redirect(url_for('first.login'))


@app_blueprint.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        # 数据库校验，用户密码是否正确
        if username == 'berg' and password == '123123':
            session['user_id'] = 1
            return redirect((url_for('first.index')))
        else:
            return redirect(url_for('first.login'))


@app_blueprint.route('/index/', methods=['GET'])
# @is_login
def index():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    p1 = 'hello,world!'
    p2 = '     hello,python!'
    # 和django不同 不需要是字典
    return render_template('index.html', list1=list1,
                           p1=p1, p2=p2)


@app_blueprint.route('/create_db/', methods=['GET'])
def create_db():
    db.create_all()
    return '创建数据库'


@app_blueprint.route('/drop_db/', methods=['GET'])
@is_login
def drop_db():
    db.drop_all()
    return '删除数据库'


@app_blueprint.route('/createstu/', methods=['POST', 'GET'])
def create_stu():
    if request.method == 'GET':
        return render_template('createstu.html')
    if request.method == 'POST':
        s_name = request.form.get('s_name')
        s_age = request.form.get('s_age')

        stu = Student()
        stu.s_name = s_name
        stu.s_age = s_age
        stu.s_create_time = datetime.now()

        # 保存
        db.session.add(stu)
        db.session.commit()
        return '创建数据成功'


@app_blueprint.route('/selectstu/', methods=['GET'])
def select_stu():
    """

    :return:
    """
    # 获取集合
   #  stus = Student.query.all()
   # # @手动实现分页， 方法1
   #  page = int(request.args.get('page',1))
   #  stus = Student.query.offset((page-1)*5).limit(5)

    # 方法2
    page = int(request.args.get('page', 1))
    # s_page = (page -1) * 5
    # e_page = page * 5
    # stus = Student.query.all()[s_page:e_page]

    # 方法3
    paginate = Student.query.paginate(page, 5, error_out=False)
    stus = paginate.items
    return render_template('stus.html', stus=stus, paginate=paginate)


@app_blueprint.route('/detailstu/<int:id>/', methods=['GET'])
def detail_stu(id):
    stu = Student.query.filter(Student.id == id)
    # filter_by 过滤
    # stu = Student.quety.filter_by(id=id)
    # get 获取不到数据也不报错
    # stu = Student.query.get(id)

    return render_template('stus.html', stus=stu)


@app_blueprint.route('/update_stu/<int:id>/', methods=['PATCH'])
def update_stu(id):
    s_name = request.form.get('s_name')

    # 第一种修改方式
    # stu = Student.query.get(id)
    # stu.s_name = s_name

    # 第二种
    Student.query.filter_by(id=id).update({'s_name': s_name})
    Student.query.filter(Student.id == id).update({'s_name': s_name})
    # db.session.add(stu)
    db.session.commit()
    return '修改数据成功'


@app_blueprint.route('/delstu/<int:id>/', methods=['DELETE'])
def del_stu(id):
    stu = Student.query.get(id)
    # stu.delete()
    db.session.delete(stu)
    db.session.commit()
    return '删除成功'


@app_blueprint.route('/sel_stu_by_sql/', methods=['GET'])
def sel_stu_by_sql():
    sql = 'select * from student'
    db.session.execute(sql)
    return '查询sql语句'


@app_blueprint.route('/create_many_stu/', methods=['POST'])
def create_many_stu():
    stu_list = []
    for i in range(10):
        stu = Student()
        stu.s_name = 'SCP%s' % (i + random.randrange(100, 500))
        stu.s_age = random.randrange(15, 20)
        stu.s_create_time = datetime.now()

        stu_list.append(stu)
        db.session.add_all(stu_list)
        # db.session.add(stu)
        db.session.commit()

    return '批量创建成功'


@app_blueprint.route('/create_init_stu/', methods=['POST'])
def create_init_stu():
    for i in range(3):
        stu = Student('SCP%s' % i, i)
        stu.save_update()
    return '创建成功'


@app_blueprint.route('/sel_stu_by_filter/', methods=['GET'])
def sel_stu_by_filter():
    # 查询学生名字中包含’2‘的学生
    # stus = Student.query.filter(Student.s_name.contains('2'))

    # stus = Student.query.filter(Student.id.in_([1, 2, 3, 4, 5]))
    # 查询年龄小于16岁学生
    # stus = Student.query.filter(Student.s_age.__lt__(16))
    # 查询姓名0结尾的学生
    # stus = Student.query.filter(Student.s_name.endswith('0')).all()
    # Student.query.filter(Student.s_name.like('%0'))
    # 模糊查询学生姓名，学生姓名第二位是’c'的学生 使用like
    # stus = Student.query.filter(Student.s_name.like('_C%')).all()
    # 查询结果按照id 降序
    # stus = Student.query.order_by('id').all()
    # stus = Student.query.order_by(-Student.id).all()
    # 查询结果安装id 升序 取5个
    # stus = Student.query.order_by(-Student.id).limit(5).all()
    # Student.query.order_by('id').limit(5)

    # 查询姓名包含S，并且年龄17的学生
    # stus = Student.query.filter(Student.s_name.contains('S'),
    #                             Student.s_age==17)
    # 姓名包含S 或 年龄为17
    # stus = Student.query.filter(or_(Student.s_age==17),
    #                             Student.s_name.contains('S'))
    # 不包含，不等于
    # stu = Student.query.filter(not_(Student.s_name.contains('S')),
    #                            not_(Student.s_age==17))
    # print(stus)
    return '查询成功'


@app_blueprint.route('/create_grade/', methods=['POST'])
def create_grade():
    g = ['Python', 'JAVA', 'C', 'C++']
    for i in g:
        grade = Grade()
        grade.g_name = i

        db.session.add(grade)
    db.session.commit()
    return '添加班级成功'


@app_blueprint.route('/stu_add_grade/<int:id>/', methods=['GET', 'POST'])
def stu_add_grade(id):
    if request.method == 'GET':
        grades = Grade.query.all()

        return render_template('addgrade.html', grades=grades)
    if request.method == 'POST':
        g_id = request.form.get('g_id')
        stu = Student.query.get(id)
        stu.g_id = g_id
        stu.save_update()
        return redirect(url_for('first.select_stu'))


@app_blueprint.route('/add_couese/', methods=['POST'])
def add_course():
    """
    添加课程
    :return:
    """
    course_list = ['语文', '数学', '英语', '音乐', '运筹学', '建筑风格', '剪力与应力']

    for i in course_list:
        courses = Course()
        courses.c_name = i

        db.session.add(courses)
    db.session.commit()

    return '创建成功'


@app_blueprint.route('/stu_add_course/<int:id>/', methods=['GET', 'POST'])
def stu_add_course(id):
    if request.method == 'GET':
        courses = Course.query.all()

        return render_template('course.html', courses=courses, )

    if request.method == 'POST':
        c_id = request.form.get('c_id')
        # 1.先找学生
        stu = Student.query.get(id)
        c = Course.query.get(c_id)
        # 2. 找关联关系stu,course
        stu.course.append(c)
        db.session.commit()
        return redirect(url_for('first.select_stu'))


@app_blueprint.route('/sel_course/<int:id>/', methods=['GET'])
def sel_course(id):
    stu = Student.query.get(id)
    courses = stu.course
    return render_template('stuCourse.html', courses=courses, id=id)


@app_blueprint.route('/del_course/<int:id>/', methods=['GET'])
def stu_del_course(id):
    c_id = request.args.get('c_id')
    course = Course.query.get(c_id)
    stu = Student.query.get(id)
    stu.course.remove(course)
    courses = stu.course
    # list 删除remove(), del list[0] pop（）
    db.session.commit()
    return render_template('stuCourse.html', id=id, courses=courses)


class StudentSource(Resource):
    def get(self, id):
        stu = Student.query.get(id)
        return {'name': stu.s_name, 'age': stu.s_age}

    def post(self, id):
        pass

    def patch(self):
        pass

    def delete(self,id):
        stu = Student.query.get(id)
        db.session.delete(stu)
        db.session.commit()
        return 'OK'

api.add_resource(StudentSource, '/api/student/<int:id>/')


# class add_stu_grade(Resource):
#     def get(self, id):
#         grades = Grade.query.all()
#
#         return render_template('addgrade.html', grades=grades)
#
#     def post(self):
#         g_id = request.form.get('g_id')
#         stu = Student.query.get(id)
#         stu.g_id = g_id
#         stu.save_update()
#         return redirect(url_for('first.select_stu'))
#
#
# api.add_resource(StudentSource, '/api/add_stu/<int:id>/')
