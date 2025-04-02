import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")  # Used for JWT
    SQLALCHEMY_DATABASE_URI = "postgresql://flask_user:flask_password@localhost/flask_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")  # JWT Key
