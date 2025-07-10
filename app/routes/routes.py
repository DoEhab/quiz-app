from flask import Blueprint, render_template, jsonify, request
from app.controllers.quiz_controller import get_quiz_q, submit_quiz_answers, get_all_quizzes
from app.utils.helper import token_required

"""
main quiz routes
"""
main = Blueprint('main', __name__)


@main.route("/")
def home():
    """
    redirects to home.html
    :return: home.html
    """
    return render_template("home.html")


@main.route('/quizzes', methods=['GET'])
@token_required
def get_quizzes():
    """
    get list of quizzes
    :return:  list of quizzes
    """
    return get_all_quizzes()


@main.route('/quiz/<quiz_id>')
def quiz_page(quiz_id):
    """
    redirection
    :return: quiz screen
    """
    return render_template("quiz.html")


@main.route('/api/quiz/<quiz_id>', methods=['GET'])
@token_required
def get_quiz(quiz_id):
    """
    get quiz by id
    :param quiz_id: selected quiz id
    :return: quiz questions
    """
    return get_quiz_q(quiz_id)


@main.route('/api/submit-quiz', methods=['POST'])
@token_required
def submit_quiz():
    """
    submit selected answers
    :return: score
    """
    return submit_quiz_answers()