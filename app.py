from flask import Flask
from flask_login import LoginManager
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['travel_website_db']

# Setup login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import routes  # Import routes

if __name__ == '__main__':
    app.run(debug=True)
