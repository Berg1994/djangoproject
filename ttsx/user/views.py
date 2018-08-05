from datetime import datetime, timedelta

from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from user.models import UserModel, UserTicket
from utils.functions import get_ticket


def register(request):
    """
    用户注册
    :param request: 客户端请求
    :return: 服务器响应
    """
    if request.method == 'GET':
        return render(request, 'back_manage/register.html')

    if request.method == 'POST':
        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        email = request.POST.get('email')
        if not all([username, pwd, cpwd, email]):
            return render(request, 'back_manage/register.html')
        if pwd != cpwd:
            return render(request, 'back_manage/register.html')
        user = UserModel.objects.create(username=username,
                                        pwd=make_password(pwd),
                                        email=email)
        return HttpResponseRedirect(reverse('user:login'))


def login(request):
    """
    用户登录
    :param request:登录请求
    :return: 服务器响应
    """
    if request.method == 'GET':
        return render(request, 'back_manage/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if not all([username, pwd]):
            return render(request, 'back_manage/login.html')
        user = UserModel.objects.filter(username=username).first()
        if user:
            if check_password(pwd, user.pwd):
                ticket = get_ticket()
                print(type(ticket))
                out_time = datetime.now() + timedelta(days=1)
                UserTicket.objects.create(ticket=ticket,
                                          user=user,
                                          out_time=out_time,
                                          )

                res = HttpResponseRedirect(reverse('index'))
                res.set_cookie('ticket', ticket, expires=out_time)

                return res


# 登出
def logout(request):
    if request.method == 'GET':
        res = HttpResponseRedirect(reverse('user:login'))
        res.delete_cookie('ticket')
        return res


# 用户中心
def user_center_info(request):
    if request.method == 'GET':
        return render(request, 'back_manage/user_center_info.html')


# 用户订单
def user_center_order(request):
    if request.method == 'GET':
        return render(request, 'back_manage/user_center_order.html')


# 用户设置
def user_center_site(request):
    if request.method == 'GET':
        return render(request, 'back_manage/user_center_site.html')
