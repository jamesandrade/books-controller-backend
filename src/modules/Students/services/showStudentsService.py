from __main__ import app

from src.modules.Students.models.Student import Student
from src.modules.Students.models.Registration import Registration
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
from app import db
import json
from sqlalchemy import func, and_

class ShowStudentsService():
    def execute(self):
        now_year = datetime.now().year
        subquery = db.session.query(
            Registration.student,
            func.max(Registration.year).label('max_year')
        ).group_by(Registration.student).subquery()
        results = db.session.query(Student, Registration)\
        .join(Registration, Student.id == Registration.student)\
        .join(subquery, and_(Registration.student == subquery.c.student, Registration.year == subquery.c.max_year))\
        .filter(Student.disabled == False)\
        .all()
        student_list = []
        for student, registration in results:
            student = student.as_dict()
            student["pending"] = True if registration.year < now_year else False
            registration = registration.as_dict()
            student["registration"] = registration
            student_list.append(student)
        return student_list

showStudentsService = ShowStudentsService()