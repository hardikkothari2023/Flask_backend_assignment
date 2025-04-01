from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import TaskManager, db

task_blueprint = Blueprint("tasks", __name__)

@task_blueprint.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    tasks = TaskManager.query.all()
    return jsonify([task.to_dict() for task in tasks])
