from django.db import models


# Create your models here.

class Grade(models.Model):
    g_name = models.CharField(max_length=10)
    g_create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'grade'


class Student(models.Model):
    s_name = models.CharField(max_length=10, null=True, unique=True)
    s_create_time = models.DateTimeField(auto_now_add=True)
    s_change_time = models.DateTimeField(auto_now=True)
    s_sex = models.BooleanField(default=1)
    g = models.ForeignKey(Grade)
    img = models.ImageField(upload_to='upload', null=True)

    class Meta:
        db_table = 'student'


# 权限
class Promission(models.Model):
    p_name = models.CharField(max_length=30,null=False)

    class Meta:
        db_table = 'promission'


class Role(models.Model):
    r_name = models.CharField(max_length=30,null=False)
    r_p = models.ManyToManyField(Promission)

    class Meta:
        db_table = 'role'


class MyUser(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=200, null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=0)
    ticket = models.CharField(max_length=30, null=True)
    #因为新加了字段R  而已经建立的数据库信息没有该字段 所以会报错  设置默认值为空可以解决
    r = models.ForeignKey(Role,null=True)

    class Meta:
        db_table = 'my_user'
