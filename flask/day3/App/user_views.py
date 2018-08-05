from flask import Blueprint, render_template, request, redirect, url_for, session

from App.models import db, Student, Grade, Course, User
from utils.decoration import is_login

from flask_restful import Resource

from utils.exts__init import api

user_blueprint = Blueprint('user', __name__)

"""
添加班级
"""


@user_blueprint.route('/add_grade/', methods=['GET', 'POST'])
def add_grade():
    if request.method == 'GET':
        return render_template('addgrade.html')
    if request.method == 'POST':
        g_name = request.form.get('g_name')
        g_dese = request.form.get('g_dese')
        grade = Grade()
        grade.g_name = g_name
        grade.g_dese = g_dese

        db.session.add(grade)
        db.session.commit()

        return '创建成功'


"""
显示所有班级
"""


@user_blueprint.route('/grade_all/')
@is_login
def grade_all():
    grades = Grade.query.all()
    return render_template('grades.html', grades=grades)


"""
通过班级创建学生
"""


@user_blueprint.route('/create_stu_by_grade/', methods=['GET', 'POST'])
def create_stu_by_grade():
    if request.method == 'GET':
        g_id = request.args.get('g_id')
        return render_template('create_student.html', g_id=g_id)

    if request.method == 'POST':
        g_id = request.form.get('g_id')
        username = request.form.get('username')

        stu = Student()
        stu.s_name = username
        stu.grades = g_id

        db.session.add(stu)
        db.session.commit()

        return redirect(url_for('user.grade_all'))


"""
通过班级查询学生
"""


@user_blueprint.route('/select_stu_by_grade/', methods=['GET'])
def select_stu_by_grade():
    if request.method == 'GET':
        g_id = request.args.get('g_id')
        g = Grade.query.get(g_id)
        stus = g.students
        return render_template('students.html', stus=stus)


"""
添加科目
"""


@user_blueprint.route('/course/', methods=['GET', 'POST'])
def course():
    courses = ['大学英语', '大学物理', '线性代数', '高数', 'VHDL', 'ARM', '马克思主义', '农场劳动']
    course_list = []

    for course in courses:
        c = Course()
        c.c_name = course
        course_list.append(c)
    db.session.add_all(course_list)
    db.session.commit()
    return '添加成功'


@user_blueprint.route('/add_course/', methods=['GET', 'POST'])
def add_course():
    if request.method == 'GET':
        # id = request.args.get('id')
        # course = Course.query.filter(c_id = id)
        courses = Course.query.all()
        return render_template('addcourses.html', courses=courses)
    if request.method == 'POST':
        s_id = request.args.get('s_id')
        course_id = request.form.get('course_id')

        stu = Student.query.get(s_id)
        course = Course.query.get(course_id)

        course.students.append(stu)

        db.session.add(course)
        db.session.commit()

        return redirect(url_for('user.grade_all'))


@user_blueprint.route('/show_course/<int:id>/', methods=['GET'])
def show_course(id):
    if request.method == 'GET':
        stu = Student.query.get(id)

        courses = stu.course
        s_id = id
        return render_template('show_course.html', courses=courses, s_id=s_id)


@user_blueprint.route('/stu/<int:s_id>/del_course/<int:c_id>/', methods=['GET'])
def del_course(c_id, s_id):
    if request.method == 'GET':
        # 删除课程号
        course = Course.query.get(c_id)
        # 删除课程的学生id
        stu = Student.query.get(s_id)
        course.students.remove(stu)
        db.session.commit()
        return redirect(url_for('user.grade_all'))


@user_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        flag = False

        if not all([username, password1, password2]):
            msg, flag = '请完整填写信息', True
        if password1 != password2:
            msg, flag = '密码错误', True
        if flag:
            return render_template('register.html', msg=msg)

        user = User(username, password1)
        user.save()

        return redirect(url_for('user.login'))


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not all([username, password]):
            msg = '请填写完整'

            return render_template('login.html', msg=msg)

        user = User.query.filter(User.username == username).first()

        if user:
            if user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('user.grade_all'))
            else:
                msg = '密码错误'
                return render_template('login.html', msg)

        else:
            msg = '用户名错误'
            return render_template('login.html', msg)


class CourseApi(Resource):

    def get(self):
        courses = Course.query.all()

        return {
            'code': 200,
            'msg': '请求成功',
            'data': [course.to_dict() for course in courses]
        }

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self, id):
        course = Course.query.get(id)
        db.session.delete(course)
        db.session.commit()
        return {'code': 200, 'msg': '删除成功'}


api.add_resource(CourseApi, '/api/course/', '/api/course/<int:id>/')
