from flask import Flask
from app.config import config
from app.extensions import db, jwt, migrate
from app.routes import register_blueprints

def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    register_blueprints(app)
    
    return app
