import os
from dotenv import load_dotenv

load_dotenv()  # Load env variables from .env file

secret_key = os.getenv("SECRET_KEY", "default_key")


def init_db():
    app.config["MONGO_URI"] = "mongodb://localhost:27017/quizapp"
    mongo.init_app(app)