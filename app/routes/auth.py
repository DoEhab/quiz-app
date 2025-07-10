from flask import Blueprint, request, redirect, render_template
from app.controllers.auth_controller import login_user, register_user
"""
auth routing
"""
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    login route
    :return: login controller data
    """
    if request.method == 'POST':
        return login_user()
    return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    signup route
    :return: signup controller response
    """
    if request.method == 'POST':
        return register_user()
    return render_template('signup.html')
