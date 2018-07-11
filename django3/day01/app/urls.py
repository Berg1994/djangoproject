from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from app import views

urlpatterns = [
   # 登录视图
    url(r'^login/$', views.login, name='login'),
    # 注册视图
    url(r'^register/$', views.register, name='register'),
    # 注销视图
    url(r'^logout/$', views.logout, name='logout'),
    # 手动实现登录注册注销
    url(r'^my_register/$', views.my_register, name='my_register'),

    url(r'^my_login/$', views.my_login, name='my_login'),

    url(r'^my_logout/$', views.my_logout, name='my_logout'),



    # 首页 login_required 登录检测
    url(r'index/', views.index, name='index'),
    # 导航栏
    url(r'left/', views.left, name='left'),
    # 班级
    url(r'^grade/$', views.grade, name='grade'),
    # 头部
    url(r'head/', views.head, name='head'),
    # 学生页面
    url(r'student/', views.student, name='student'),
    # 添加学生
    url(r'addstu/', views.addstu, name='addstu'),
    # 添加班级
    url(r'addgrade/', views.addgrade, name='addgrade'),
    # 删除学生
    url(r'delstu/', views.delstu, name='delstu'),
    # 编辑学生
    url(r'editgrade/', views.editgrade, name='editgrade'),

    #测试
    url(r'test/',views.test,name='test')

]
