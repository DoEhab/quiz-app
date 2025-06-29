from flask_cors import CORS

from app.utils.db import init_db
from app.routes.routes import main
from app.routes.auth import auth


def create_app():
    from flask import Flask
    app = Flask(__name__)
    #to do: change this to one domain name
    CORS(app, supports_credentials=True, origins=["http://localhost:63342"])
    app.register_blueprint(main)
    app.register_blueprint(auth)
    init_db(app)
    return app
