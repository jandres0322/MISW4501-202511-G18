import requests
import os
from flask import request
from app.exceptions.http_exceptions import UnauthorizedError, NotFoundError, ForbiddenError
from app.utils.response_util import format_response

USER_SERVICE_URL = f"{os.getenv('USER_SERVICE_URL')}/verify"

def check_auth(token):
    response = requests.get(USER_SERVICE_URL, headers={"Authorization": token})
    if response.status_code == 401:
        raise UnauthorizedError(response.json()["error"])
    if response.status_code == 403:
        raise ForbiddenError(response.json()["error"])
    if response.status_code == 404:
        raise NotFoundError(response.json()["error"])

def auth_required(func):
    def decorated_function():
        try:
            token = request.headers.get("Authorization")
            if not token:
                raise UnauthorizedError("Token no enviado")
            check_auth(token)
        except (UnauthorizedError, NotFoundError, ForbiddenError) as e:
            return format_response("error", e.code, error=e.description)
        else:
            return func()
    return decorated_function