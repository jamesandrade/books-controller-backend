from __main__ import app

from src.modules.Users.models.User import User
from app import db

class ShowUserService():
    def execute(self, data):
        user = User.query.filter_by(id=data).first()
        return user.as_dict() if user else []

showUserService = ShowUserService()