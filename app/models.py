from pymongo import MongoClient
from flask_bcrypt import Bcrypt

client = MongoClient('mongodb://localhost:27017/')
db = client['travel_website_db']
bcrypt = Bcrypt()

class User:
    @staticmethod
    def create_user(username, password):
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        db.users.insert_one({'username': username, 'password': hashed_pw})
    
    @staticmethod
    def validate_user(username, password):
        user = db.users.find_one({'username': username})
        if user and bcrypt.check_password_hash(user['password'], password):
            return user
        return None
