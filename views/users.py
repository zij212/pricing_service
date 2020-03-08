from flask import Blueprint, request, session, url_for, render_template, redirect
from models.user import User, UserErrors
# models/user is a directory, when importing it,
# it will load up packages loaded in models/user/__init__.py
# which includes the following two lines
# from models.user.user import User
# import models.user.erros as UserErrors

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            User.register_user(email, password)
            session['email'] = email
            return email
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/register.html')


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            User.is_login_valid(email, password)
            session['email'] = email
            return email
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/login.html')


@user_blueprint.route('/logout', methods=['GET', 'POST'])
def logout_user():
    session['email'] = None
    return redirect(url_for('.login_user'))
