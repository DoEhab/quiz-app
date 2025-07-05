from bson import ObjectId
from flask import Blueprint, render_template, jsonify

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
    quizzes = list(mongo.db.quizzes.find({}, {'title': 1, 'topic': 1}))  # select fields only
    for quiz in quizzes:
        quiz['_id'] = str(quiz['_id'])  # convert ObjectId to string
    return jsonify(quizzes), 200


@main.route('/quiz/<quiz_id>')
def quiz_page(quiz_id):
    return render_template("quiz.html")  # static HTML shell


@main.route('/api/quiz/<quiz_id>', methods=['GET'])
@token_required
def get_quiz(quiz_id):
    quiz = mongo.db.quizzes.find_one({'_id': ObjectId(quiz_id)})
    if not quiz:
        return jsonify({'error': 'Quiz not found'}), 404

    quiz['_id'] = str(quiz['_id'])
    return jsonify({
        'title': quiz['title'],
        'topic': quiz['topic'],
        'questions': quiz['questions']
    }), 200
