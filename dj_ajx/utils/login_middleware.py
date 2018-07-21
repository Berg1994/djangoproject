import re

from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse
from users.models import UserTicketModel
from django.http import HttpResponseRedirect
from datetime import datetime


class UserMiddle(MiddlewareMixin):
    # 重构方法
    def process_request(self, request):
        # 验证用户的登录信息
        paths = ['/user/login/', '/user/register/',
                 '/axf/market/', '/axf/marketparams/(\d+)/(\d+)/(\d+)/']
        # if request.path in paths:
        for path in paths:
            if re.match(path, request.path):
                return None
        else:
            ticket = request.COOKIES.get('ticket')
            if not ticket:
                return HttpResponseRedirect(reverse('user:login'))

            ticket_user = UserTicketModel.objects.filter(ticket=ticket).first()
            if not ticket_user:
                return HttpResponseRedirect(reverse('user:login'))

            if ticket_user.out_time.replace(tzinfo=None) < datetime.now():
                ticket_user.delete()
                return HttpResponseRedirect(reverse('user:login'))

            request.user = ticket_user.user
