from __main__ import app

import os
import cryptocode
from cryptography.hazmat.primitives import serialization
from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask import jsonify

from src.infra.errors.app_error import AppError
from src.modules.Users.models.User import User
from app import db

class LoginService():
    def execute(self, data):
        user = User.query.filter_by(email=data.get("email", None)).first()
        if not user:
            return AppError(message="User does not exists", statusCode=404).error()
        if user.active is False:
            return AppError(message="User disabled", statusCode=401).error()
        if cryptocode.decrypt(user.password, os.environ['PASSW_SECRET']) != data.get("password", None):
            return AppError(message="Password does not match", statusCode=401).error()
        payload = {
            "user_id": user.id,
            "username": user.username,
            "level": user.level,
        }
        access_token = create_access_token(identity=user.id,
                                           additional_claims=payload,
                                           expires_delta=timedelta(days=15)
                                           )

        return jsonify(token=access_token)
loginService = LoginService()