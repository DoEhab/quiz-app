from bson import ObjectId
from flask import jsonify, request, Blueprint

from app.utils.db import mongo
from app.utils.helper import token_required

quiz = Blueprint('quiz', __name__)


@quiz.route('/api/quiz/<quiz_id>', methods=['GET'])
@token_required
def get_quiz_q(quiz_id):
    quiz_data = mongo.db.quizzes.find_one({'_id': ObjectId(quiz_id)})
    if not quiz:
        return jsonify({'error': 'Quiz not found'}), 404

    quiz_data['_id'] = str(quiz_data['_id'])
    return jsonify({
        'title': quiz_data['title'],
        'topic': quiz_data['topic'],
        'questions': quiz_data['questions']
    }), 200


@quiz.route('/api/submit-quiz', methods=['POST'])
@token_required
def submit_quiz_answers():
    data = request.get_json()
    quiz_id = data.get('quizId')
    answers = data.get('answers')
    score = data.get('score')
    total = data.get('total')

    if not all([quiz_id, answers, score is not None, total]):
        return jsonify({'error': 'Missing data'}), 400

    submission = {
        'user_id': request.user_id,
        'quiz_id': quiz_id,
        'score': score,
        'total': total,
        'answers': answers,
    }

    mongo.db.submissions.insert_one(submission)
    return jsonify({'message': 'Quiz submitted successfully'}), 201
