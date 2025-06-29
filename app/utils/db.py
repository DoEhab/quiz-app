import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo

load_dotenv()

mongo = PyMongo()

secret_key = os.getenv("SECRET_KEY", "default_key")


def init_db(app):
    """
    Initializes MongoDB connection with Flask app.
    """
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/quiz_db")
    mongo.init_app(app)
