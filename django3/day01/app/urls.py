from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from app import views

urlpatterns = [
    # 登录视图
    url(r'login/', views.login, name='login'),
    # 注册视图
    url(r'register/', views.register, name='register'),
    # 注销视图
    url(r'logout/', views.logout, name='logout'),
    # 首页 login_required 登录检测
    url(r'index/', login_required(views.index), name='index'),
    # 导航栏
    url(r'left/', views.left, name='left'),
    # 班级
    url(r'^grade/$', views.grade, name='grade'),
    # 头部
    url(r'head/', views.head, name='head'),
    #学生页面
    url(r'student/', views.student, name='student'),
    #添加学生
    url(r'addstu/', views.addstu, name='addstu'),
    #添加班级
    url(r'addgrade/', views.addgrade, name='addgrade'),

]
