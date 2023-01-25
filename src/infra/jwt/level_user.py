from __main__ import app

from src.modules.Users.models.User import User

from app import db
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt
from flask import jsonify, request
from src.infra.errors.app_error import AppError
def level_user():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            level = claims["level"]
            user_id = claims["user_id"]
            _, route, sys_id = request.path.split('/')
            if (level == 5) or (route == 'users' and level == 1 and sys_id == user_id):
                return fn(*args, **kwargs)
            else:
                tenant_id = claims["tenant_id"]
                if (level > 1 and route=='users'):
                    user = User.query.filter_by(id=sys_id).first()
                    if user and str(user.tenant_id) == tenant_id:
                        return fn(*args, **kwargs)
                elif (level > 1 and route=='tenants' and tenant_id==sys_id):
                        return fn(*args, **kwargs)
                else:
                    return AppError(message="Your level is not compatible", statusCode=401).error()

        return decorator

    return wrapper