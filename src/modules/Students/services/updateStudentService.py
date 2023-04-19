from __main__ import app
import os
from sqlalchemy import exc
from datetime import datetime
import pytz
import re

from src.modules.Students.models.Student import Student
from src.modules.Students.models.Registration import Registration

from src.infra.errors.app_error import AppError
from app import db

class UpdateStudentService():

    def execute(self, data):
        try:
            date_now = datetime.now(pytz.timezone('America/Sao_Paulo'))
            student = {}
            student.update(data)
            student.pop('team')
            student.pop('period')
            student.pop('user_id')
            student['updated_at'] = date_now
            student['updated_by'] = data["user_id"]
            updatedStudent = Student.query.filter_by(ra = data["ra"])
            id_student = updatedStudent.first().id
            updatedStudent.update(student)
            db.session.commit()
            registration = {}
            registration["team"] = data["team"]
            registration["period"] = data["period"]
            registration["student"] = id_student
            updatedRegistration = Registration.query.filter_by(
                year = date_now.year,
                student = id_student
            )
            if updatedRegistration.first() is None:
                registration['created_by'] = data["user_id"]
                newRegistration = Registration(**registration)
                db.session.add(newRegistration)
                db.session.commit()
            else:
                registration['updated_by'] = data["user_id"]
                registration['updated_at'] = date_now
                updatedRegistration.update(registration)
                db.session.commit()
            return [student, registration]
        except exc.IntegrityError:
            db.session.rollback()
            return AppError(message="Integrity Error", statusCode=409).error()
        except:
            db.session.rollback()
            return AppError(message="Default Error", statusCode=500).error()

updateStudentService = UpdateStudentService()