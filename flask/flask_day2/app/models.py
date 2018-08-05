# db 源于sqlalchemy
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

# 创建实例
db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(10), nullable=False)
    s_age = db.Column(db.INTEGER, nullable=True)
    s_create_time = db.Column(db.DateTime)
    # 外键写在多的一方
    g_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=True)

    # 如果不设置  默认就是Student  django 是app_tablename
    __tablename__ = 'student'
    #
    # def __init__(self, name, age):
    #     self.s_name = name
    #     self.s_age = age
    #     self.s_create_time = datetime.now()

    def save_update(self):
        db.session.add(self)
        db.session.commit()


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(10), nullable=False)
    g_create_time = db.Column(db.DateTime, default=datetime.now())
    # 关系写在一对多 一的这边 关联第一个参数是模型名 没有__tablename__ 不能小写
    stu = db.relationship('Student', backref='grade', lazy=True)


# 中间表写在两个关系表之间  这样secondary 才能赋值到表名
c_s = db.Table('stu_course',
               db.Column('s_id',
                         db.Integer,
                         db.ForeignKey('student.id'),
                         primary_key=True),
               db.Column('c_id',
                         db.Integer,
                         db.ForeignKey('course.id'),
                         primary_key=True)
               )


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(10), nullable=False)
    c_desc = db.Column(db.String(20), nullable=True)
    stu = db.relationship('Student', secondary=c_s, backref='course', lazy=True)
    __tablename__ = 'course'
