from __main__ import app
import os
import cryptocode
from sqlalchemy import exc

from src.infra.errors.app_error import AppError
from src.modules.Users.models.User import User
from app import db

class CreateUserService():
    def execute(self, data):
        hashedPassword = cryptocode.encrypt(data.get('password'), os.environ['PASSW_SECRET'])
        data["password"] = hashedPassword
        data["username"] = data["username"].title()
        try:
            newUser = User(**data)
            db.session.add(newUser)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            return AppError(message="Integrity Error", statusCode=409).error()
        except:
            db.session.rollback()
            return AppError(message="Default Error", statusCode=500).error()

        return newUser.as_dict()

createUserService = CreateUserService()