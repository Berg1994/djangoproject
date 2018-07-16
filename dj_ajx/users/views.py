from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
# 个人主页
from users.models import UserModel, UserTicketModel
from utils.functions import get_ticket


def mine(request):
    if request.method == 'GET':
        return render(request, 'mine/mine.html')


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'user/user_register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        icon = request.FILES.get('icon')

        if not all([username, email, password, icon]):
            msg = '请填写完整'
            return render(request, 'user/user_register.html', {'msg': msg})
        password = make_password(password)
        user = UserModel.objects.create(username=username,
                                        email=email,
                                        password=password,
                                        icon=icon,
                                        )
        return HttpResponseRedirect(reverse('user:login'))


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'user/user_login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([username, password]):
            msg = '请填写完整'
            return render(request, 'user/user_login.html', {'msg': msg})
        user = UserModel.objects.filter(username=username).first()
        if user:
            # checkpassword 返回布尔值  前面填获取的密码 后面是服务器已经加密的密码
            if check_password(password, user.password):
                ticket = get_ticket()
                res = HttpResponseRedirect(reverse('user:mine'))
                # 当前时间加1天
                out_time = datetime.now() + timedelta(days=1)
                # max_age为最大存活时间  expires 是什么时候到期
                res.set_cookie('ticket', ticket, expires=out_time)
                UserTicketModel.objects.create(user=user,
                                               ticket=ticket,
                                               out_time=out_time)

                return res
            msg = '账号或者密码错误'
            return render(request, 'user/user_login.html', {'msg': msg})
        msg = '账号或者密码错误'
        return render(request, 'user/user_login.html', {'msg': msg})