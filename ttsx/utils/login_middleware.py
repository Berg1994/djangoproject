from datetime import datetime

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from user.models import UserTicket


class UserMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        check_path = ['/', '/user/login/', '/user/register/']
        if request.path in check_path:
            return None
        else:
            ticket = request.COOKIES.get('ticket')
            if not ticket:
                return HttpResponseRedirect(reverse('user:login'))

            ticket_user = UserTicket.objects.filter(ticket=ticket).first()

            if not ticket_user:
                return HttpResponseRedirect(reverse('user:login'))

            if ticket_user.out_time.replace(tzinfo=None) < datetime.now():
                ticket_user.delete()
                return HttpResponseRedirect(reverse('user:login'))

            request.user = ticket_user.user
