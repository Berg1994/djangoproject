import random

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from app.models import MyUser


def is_login(func):
    def check_login(request):
        ticket = request.COOKIES.get('ticket')

        if ticket:
            user = MyUser.objects.filter(ticket=ticket).first()
            if user:
                # request.user = user
                return func(request)
            else:
                return HttpResponseRedirect(reverse('app:my_login'))
        else:

            return HttpResponseRedirect(reverse('app:my_login'))

    return check_login


def get_ticket():
    ticket = ''
    s = '1234567890qazwsxedcrfvtgbyhnujmikolp'
    for i in range(25):
        ticket += random.choice(s)
    return ticket
