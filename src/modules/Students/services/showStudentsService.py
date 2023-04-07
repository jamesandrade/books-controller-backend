from __main__ import app

from src.modules.Students.models.Student import Student
from app import db

class ShowStudentsService():
    def execute(self):
        students = Student.query.all()
        students_list = []
        for student in students:
            students_list.append(student.as_dict()) 
        return students_list

showStudentsService = ShowStudentsService()