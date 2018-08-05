from flask import redirect, url_for, session
from functools import wraps


def get_sqlalchemy_uri(DATABASE):
    return '%s+%s://%s:%s@%s:%s/%s' % (DATABASE['ENGINE'],
                                       DATABASE['DRIVER'],
                                       DATABASE['USER'],
                                       DATABASE['PASSWORD'],
                                       DATABASE['HOST'],
                                       DATABASE['PORT'],
                                       DATABASE['DB'],
                                       )


def is_login(func):
    # 因为被装饰的函数需要使用各种参数
    @wraps(func)
    def check_login(*args, **kwargs):
        if 'user_id' in session:
            return func(*args, **kwargs)
        else:
            redirect(url_for('my_user.login'))

    return check_login
