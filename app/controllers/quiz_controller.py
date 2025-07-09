from bson import ObjectId
from flask import jsonify, request, Blueprint

from app.utils.db import mongo
from app.utils.helper import token_required
"""
This file has all quiz logic
"""
quiz = Blueprint('quiz', __name__)


@quiz.route('/quizzes', methods=['GET'])
@token_required
def get_all_quizzes():
    """
    list of all quizzes
    :return: list of quizzes with its data
    """
    user_id = request.user_id
    quizzes = list(mongo.db.quizzes.find({}, {'title': 1, 'topic': 1}))

    for quiz_data in quizzes:
        quiz_data['_id'] = str(quiz_data['_id'])
        submission = mongo.db.submissions.find_one(
            {'user_id': user_id, 'quiz_id': quiz_data['_id']},
            sort=[('_id', -1)]
        )
        if submission:
            quiz_data['score'] = submission['score']
            quiz_data['total'] = submission['total']
            quiz_data['date'] = submission['_id'].generation_time.strftime('%Y-%m-%d %H:%M')
        else:
            quiz_data['score'] = None
            quiz_data['total'] = None
            quiz_data['date'] = None

    return jsonify(quizzes), 200


@quiz.route('/api/quiz/<quiz_id>', methods=['GET'])
@token_required
def get_quiz_q(quiz_id):
    """
    get the quiz questions
    :param quiz_id: the id of the selected quiz
    :return: quiz title, topic and questions
    """
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
    """
    submits the selected answers
    :return: scores and correct answer
    """
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
