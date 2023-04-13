from __main__ import app
import os
from sqlalchemy import exc
from datetime import datetime
import re

from src.modules.Students.models.Student import Student
from src.modules.Students.models.Registration import Registration

from src.infra.errors.app_error import AppError
from app import db

class CreateStudentService():

    def execute(self, data):
        try:
            student = {}
            student.update(data)
            student.pop('team')
            student.pop('period')
            student.pop('user_id')
            student['created_by'] = data["user_id"]
            student["disabled"] = False
            student["ra"] = self.createRa(data["team"], data["period"])
            newStudent = Student(**student)
            db.session.add(newStudent)
            db.session.commit()
            registration = {}
            registration["team"] = data["team"]
            registration["period"] = data["period"]
            registration["student"] = newStudent.id
            registration['created_by'] = data["user_id"]
            newRegistration = Registration(**registration)
            db.session.add(newRegistration)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            return AppError(message="Integrity Error", statusCode=409).error()
        except:
            db.session.rollback()
            return AppError(message="Default Error", statusCode=500).error()

        return newStudent.as_dict()
    def createRa(self, team, period):
        periods = {
            "Matutino": 1,
            "Vespertino": 2,
            "Noturno": 3
        }
        year = str(datetime.now().year)
        team_number = str(re.findall('\d+', team)[0] if re.findall('\d+', team) else 0)
        period_number = str(periods.get(period, 0))
        students_number = str(Student.query.count() + 1)
        return  year + team_number + period_number + students_number
createStudentService = CreateStudentService()