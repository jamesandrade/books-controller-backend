from __main__ import app
import os
from sqlalchemy import exc
from src.modules.Students.models.Student import Student
from src.infra.errors.app_error import AppError
from app import db

class CreateStudentService():
    def execute(self, data):
        try:
            newStudent = Student(**data)
            db.session.add(newStudent)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            return AppError(message="Integrity Error", statusCode=409).error()
        except:
            db.session.rollback()
            return AppError(message="Default Error", statusCode=500).error()

        return newStudent.as_dict()

createStudentService = CreateStudentService()