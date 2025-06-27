from utils.db import mongo

def get_user_by_email(email):
    return mongo.db.users.find_one({"email": email})

def create_user(email, hashed_pw):
    return mongo.db.users.insert_one({"email": email, "password": hashed_pw})

def get_all_questions():
    return list(mongo.db.questions.find())
