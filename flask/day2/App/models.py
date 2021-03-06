from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    s_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    s_name = db.Column(db.String(16), unique=True)
    s_age = db.Column(db.Integer, default=18)

    __tablename__ = 'student'


class UserModel(db.Model):
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(30))
    password = db.Column(db.String(100))

    __tablename__ = 'user'
