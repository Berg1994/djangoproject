from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

from users.models import UserTicketModel


class UserMiddle(MiddlewareMixin):

    def process_request(self, request):

        check_path = ['/axf/mine']

        for path in check_path:
            if request.path == path:
                ticket = request.COOKIE.get('ticekt')
                if ticket:
                    ticket_user = UserTicketModel.objects.filter(ticket=ticket).first()
                    if ticket_user:
                        request.user = ticket_user.user
                        return None
                    return render(request, 'user/user_login.html')
                return render(request, 'user/user_login.html')

            return None
