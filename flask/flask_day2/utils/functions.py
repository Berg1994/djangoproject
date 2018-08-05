from flask import session, redirect, url_for


def is_login(func):
    def is_log(*args, **kwargs):
        if 'user_id' in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('app.login'))

    return is_log
