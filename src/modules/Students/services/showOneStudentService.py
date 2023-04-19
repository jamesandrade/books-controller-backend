from __main__ import app

from src.modules.Students.models.Student import Student
from src.modules.Students.models.Registration import Registration
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
from app import db
import json
from sqlalchemy import func, and_

class ShowOneStudentService():
    def execute(self, ra):
        now_year = datetime.now().year
        result = Student.query.filter(Student.ra == ra).first()
        if result is None:
            return {}
        result = result.as_dict()
        result["pending"] = True if result["registration"]["year"] < now_year else False
        return result

showOneStudentService = ShowOneStudentService()