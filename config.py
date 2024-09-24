import os

class Config:
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

    # MongoDB settings
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/travel_website_db')

    # Additional configuration (optional)
    DEBUG = True
    SESSION_COOKIE_SECURE = True  # Securing session cookies

