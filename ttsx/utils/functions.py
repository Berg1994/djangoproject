from random import choice


def get_ticket():
    ticket = ''
    ticket_num = '123456789qwertyuiopasdfghjklzxcvbnm'

    for i in range(28):
        i = choice(ticket_num)
        ticket += i
    return ticket
