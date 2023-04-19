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
        results = db.session.query(Student).all()
        student_list = []
        for student in results:
            student = student.as_dict()
            student["pending"] = True if student["registration"]["year"] < now_year else False
            student_list.append(student)
        return student_list

showStudentsService = ShowStudentsService()