from flask import Blueprint, request, jsonify

from models.users_models import UserModel

def create_user_routes(db):
    user_bp = Blueprint("users", __name__)
    user_model = UserModel(db)

    @user_bp.route("/users", methods=["POST"])
    def create_user():
        data = request.json
        user_id = user_model.create_user(data["username"])
        return jsonify({"message": "User created", "user_id": str(user_id)}), 201

    @user_bp.route("/users/<username>", methods=["GET"])
    def get_user(username):
        user = user_model.get_user(username)
        if user:
            return jsonify(user), 200
        return jsonify({"error": "User not found"}), 404

    return user_bp
