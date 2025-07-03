from flask import Blueprint, render_template

from app.utils.helper import token_required

# Create a Blueprint
main = Blueprint('main', __name__)


@main.route("/")
def home():
    return render_template("home.html")
