from flask import session, redirect, url_for


# 此处为装饰器 func参数是你要包装的函数作为参数
def is_login(func):
    def check_login():
        user_session = session.get('user_id')
        if user_session:
            return func()
        else:
            # return redirect(url_for('user.login'))
            return redirect(url_for('user.login'))

    return check_login
