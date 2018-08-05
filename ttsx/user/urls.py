from django.conf.urls import url

from user import views

urlpatterns = [
    # 注册
    url('register/', views.register, name='register'),
    # 登录
    url('login/', views.login, name='login'),
    # 注销
    url('logout/', views.logout, name='logout'),
    # 用户中心
    url(r'^user_center_info/', views.user_center_info, name='user_center_info'),
    # 用户订单
    url(r'^user_center_order/', views.user_center_order, name='user_center_order'),
    # 用户信息设置
    url(r'^user_center_site/', views.user_center_site, name='user_center_site'),

]
