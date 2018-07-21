import random
from datetime import datetime


def get_ticket():
    ticket = ''
    ticket_list = '1234567890qazwsxedcrfvtgbyhnujmikolp'
    for i in range(28):
        i = random.choice(ticket_list)
        ticket += i
    return ticket


def get_order_num():
    num = ''
    ticket_list = '1234567890qazwsxedcrfvtgbyhnujmikolp'
    for i in range(10):
        i = random.choice(ticket_list)
        num += i
    order_title = datetime.now().strftime('%Y%m%d%H%M%S')
    return order_title + num
