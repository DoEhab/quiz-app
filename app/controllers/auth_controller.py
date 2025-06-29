from flask import request, redirect, url_for, flash, session, jsonify
from app.utils.db import mongo
import hashlib


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

        if user:
            session['user_id'] = str(user['_id'])
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401

    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({"error": "Internal server error"}), 500


def register_user():
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_pw = hashlib.sha1(password.encode()).hexdigest()

    if mongo.db.users.find_one({'email': email}):
        flash('Email already registered')
        return redirect(url_for('auth.signup'))

    mongo.db.users.insert_one({'email': email, 'password': hashed_pw})
    flash('Account created')
    return redirect(url_for('auth.login'))
