from src.modules.Loans.models.Loan import Loan
from src.modules.Students.models.Student import Student
from app import db

class ShowStudentsWithLoan():
    def execute(self):
        results = db.session.query(Student).join(Loan).filter(Loan.returned == False).all()
        students = []
        for result in results:
            students.append(result.as_dict())
        return students

showStudentsWithLoan = ShowStudentsWithLoan()
