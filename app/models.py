from app.utils.db import mongo

"""
Authentication models
Contains authentication database queries
"""


def get_user_by_email(email, hashed_pw):
    """
    get user by email and password
    :param email: user email
    :param hashed_pw: user hashed password
    :return: user object
    """
    return mongo.db.users.find_one({'email': email, 'password': hashed_pw})


def create_user(first_name, last_name, email, hashed_pw):
    """
    register new account
    :param first_name: username
    :param last_name: user last name
    :param email: user email
    :param hashed_pw: user hashed password
    :return: none
    """
    return mongo.db.users.insert_one({
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': hashed_pw
    })
