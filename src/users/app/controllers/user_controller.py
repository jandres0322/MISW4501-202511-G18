from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.models.user_model import UserSchema

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_bp.route('/', methods=['GET'])
def get_users():
    users = UserService.get_all()
    return jsonify(users_schema.dump(users))

@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id:int):
    return 'get user'