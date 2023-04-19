from src.modules.Loans.models.Loan import Loan
from src.modules.Students.models.Student import Student
from app import db

class ShowStudentLoans():
    def execute(self, ra):
        results = Loan.query.join(Student).filter(Student.ra == ra, Loan.returned == False).all()
        loans = []
        for result in results:
            result = result.as_dict()
            result.pop("student")
            loans.append(result)
        return loans

showStudentLoans = ShowStudentLoans()
