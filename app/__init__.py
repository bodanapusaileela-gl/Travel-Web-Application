from flask import Flask
from config import Config
from pymongo import MongoClient
##from dotenv import load_dotenv
import os

# Load environment variables from .env
#load_dotenv()

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize MongoDB
client = MongoClient(app.config['MONGO_URI'])
db = client.get_default_database()

# Import routes here to avoid circular imports
from app import routes

