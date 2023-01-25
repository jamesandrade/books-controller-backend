from __main__ import app

import os
import cryptocode

from src.infra.errors.app_error import AppError
from src.modules.Users.models.User import User
from app import db

class UpdateUserService():
    def execute(self, user_id, data):
        user = User.query.filter_by(id=user_id)
        if not user.first():
            return AppError(message="User does not exists", statusCode=404).error()
        if "password" in data:
            hashedPassword = cryptocode.encrypt(data.get('password'), os.environ['PASSW_SECRET'])
            data["password"] = hashedPassword
        if "username" in data:
            data["username"] = data["username"].title()
        try:
            user.update(dict(data))
            db.session.commit()
        except:
            db.session.rollback()
            return AppError(message="Default Error", statusCode=500).error()

        updateddata = user.first()
        return updateddata.as_dict()

updateUserService = UpdateUserService()