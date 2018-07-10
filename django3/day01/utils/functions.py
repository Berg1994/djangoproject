from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from app.models import MyUser


def is_login(func):
    def check_login(request):
        # 判断如果登录则返回函数

        ticket = request.COOKIES.get('ticket')

        if not ticket:
            return HttpResponseRedirect(reverse('app:my_login'))
        user = MyUser.objects.filter(ticket=ticket)
        if not user:
            return HttpResponseRedirect(reverse('app:my_login'))
        return func(request)

    return check_login
