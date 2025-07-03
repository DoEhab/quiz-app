import jwt
import datetime
import os
from flask import request, jsonify, url_for, redirect
from functools import wraps

SECRET_KEY = os.getenv("SECRET_KEY", "default_key")


def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def decode_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}, 401
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}, 401


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Expecting token in header as: Authorization: Bearer <token>
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.user_id = decoded['user_id']
        except jwt.ExpiredSignatureError:
            return redirect(url_for('auth.login'))
        except jwt.InvalidTokenError:
            return redirect(url_for('auth.login'))

        return f(*args, **kwargs)

    return decorated
