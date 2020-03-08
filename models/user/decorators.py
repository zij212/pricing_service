import functools
from typing import Callable
from flask import session, flash, redirect, url_for, current_app


def requires_login(f: Callable) -> Callable:
    # need the functools decorator to keep the orginal function's name and docstring
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('email'):
            # flash put the warning message in a queue and can be accessed by the views (.hyml)
            flash('You need to be signed in for this page',
                  'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_function # not brackets!


def requires_admin(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_fucntion(*args, **kwargs):
        if session.get('email') != current_app.config.get('ADMIN', ''):
            flash('You need to be an administrator to access this page', 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)

    return decorated_fucntion


