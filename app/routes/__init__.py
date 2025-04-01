from flask import Blueprint

def register_blueprints(app):
    from app.routes.task_routes import task_blueprint
    app.register_blueprint(task_blueprint)
