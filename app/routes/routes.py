from flask import Blueprint, render_template

# Create a Blueprint
main = Blueprint('main', __name__)


@main.route("/")
def home():
    return render_template("login.html")
