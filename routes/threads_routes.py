from flask import Blueprint, request, jsonify

from models.threads_models import ThreadModel

def create_thread_routes(db):
    thread_bp = Blueprint("threads", __name__)
    thread_model = ThreadModel(db)

    @thread_bp.route("/threads", methods=["POST"])
    def create_thread():
        data = request.json
        thread_id = thread_model.create_thread(data["user_id"], data["content"])
        return jsonify({"message": "Thread created", "thread_id": str(thread_id)}), 201

    @thread_bp.route("/threads", methods=["GET"])
    def get_threads():
        return jsonify(thread_model.get_all_threads()), 200

    @thread_bp.route("/threads/<user_id>", methods=["GET"])
    def get_user_threads(user_id):
        return jsonify(thread_model.get_user_threads(user_id)), 200

    return thread_bp
