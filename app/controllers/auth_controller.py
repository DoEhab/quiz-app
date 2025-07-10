from flask import request, jsonify

from app.models import get_user_by_email, create_user
from app.utils.db import mongo
from app.utils.helper import generate_token, hash_pass

"""
This file contains all authentication logic
"""


def login_user():
    """
    Handles the login logic
    :return: json response and status code
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        hashed_pw = hash_pass(password)
        user = get_user_by_email(email, hashed_pw)
        if not user:
            return jsonify({'error': 'This account doesn\'t exist'}), 401

        token = generate_token(str(user['_id']))
        print(token)
        return jsonify({'token': token}), 200

    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({"error": "Internal server error"}), 500


def register_user():
    """
    new account logic
    :return: json response and status code
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')

    if not all([first_name, last_name, email, password]):
        return jsonify({"error": "All fields are required"}), 400

    if mongo.db.users.find_one({'email': email}):
        return jsonify({"error": "Email already exists"}), 400

    hashed_pw = hash_pass(password)

    try:
        create_user(first_name, last_name, email, hashed_pw)
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        print(f"Error creating user: {e}")
        return jsonify({"error": "An error occurred while registering user"}), 500
