from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from app.exceptions.http_exceptions import UnauthorizedError, BadRequestError, ForbiddenError
from app.utils.response_util import format_response
from app.services.user_service import UserService
from app.models.user_model import UserSchema

auth_bp = Blueprint('auth', __name__)
user_schema = UserSchema(only=("name", "lastname", "email", "username"))

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        user_data = request.get_json()
        user = UserService.check_credentials(user_data)
    except UnauthorizedError as e:
        return format_response("error", e.code, error=e.description)
    except BadRequestError as e:
        return format_response("error", e.code, error=e.description)
    except ForbiddenError as e:
        return format_response("error", e.code, error=e.description)
    else:
        response: dict = {
            "user": user_schema.dump(user),
            "access_token": create_access_token(identity=user.id)
        }
        return format_response("success", 200, message="Usuario logueado con éxito", data=response)
