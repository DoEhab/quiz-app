from flask import request, redirect, url_for, flash, session, jsonify
from app.utils.db import mongo
import hashlib

from app.utils.helper import generate_token


def login_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        hashed_pw = hashlib.sha1(password.encode()).hexdigest()
        user = mongo.db.users.find_one({'email': email, 'password': hashed_pw})
        if not user:
            return jsonify({'error': 'Invalid credentials'}), 401

        token = generate_token(str(user['_id']))
        print(token)
        return jsonify({'token': token}), 200

    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({"error": "Internal server error"}), 500


def register_user():
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

    hashed_pw = hashlib.sha1(password.encode()).hexdigest()

    mongo.db.users.insert_one({
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': hashed_pw
    })

    return jsonify({"message": "User registered successfully"}), 201
