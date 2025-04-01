from flask import Blueprint, jsonify

task_bp = Blueprint("task", __name__)

@task_bp.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "Pong!"})
