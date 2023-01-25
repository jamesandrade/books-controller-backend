from __main__ import app

from src.infra.errors.app_error import AppError
from src.modules.Users.models.User import User
from app import db

class DisableUserService():
    def execute(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return AppError(message="User does not exists", statusCode=404).error()
        try:
            user.active = False
            db.session.commit()
        except:
            db.session.rollback()
            return AppError(message="Default Error", statusCode=500).error()

        return user.as_dict()

disableUserService = DisableUserService()