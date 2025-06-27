from app.utils.db import init_db


def create_app():
    from flask import Flask
    app = Flask(__name__)
    init_db()
    return app
