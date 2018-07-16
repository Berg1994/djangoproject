import random


def get_ticket():
    ticket = ''
    ticket_list = '1234567890qazwsxedcrfvtgbyhnujmikolp'
    for i in range(28):
        i = random.choice(ticket_list)
        ticket += i
    return ticket

