from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.extensions import db  # Import db from extensions
from app.models import User  # Register models

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    
    db.init_app(app)  # Initialize database
    Migrate(app, db)  # Initialize migrations

    with app.app_context():
        db.create_all()  # Try to create tables

    return app
