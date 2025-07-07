from bson import ObjectId
from flask import Blueprint, render_template, jsonify, request

from app.controllers.quiz_controller import get_quiz_q, submit_quiz_answers, get_all_quizzes
from app.utils.db import mongo
from app.utils.helper import token_required

# Create a Blueprint
main = Blueprint('main', __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route('/quizzes', methods=['GET'])
@token_required
def get_quizzes():
    return get_all_quizzes()


@main.route('/quiz/<quiz_id>')
def quiz_page(quiz_id):
    return render_template("quiz.html")  # static HTML shell


@main.route('/api/quiz/<quiz_id>', methods=['GET'])
@token_required
def get_quiz(quiz_id):
    return get_quiz_q(quiz_id)


@main.route('/api/submit-quiz', methods=['POST'])
@token_required
def submit_quiz():
    return submit_quiz_answers()