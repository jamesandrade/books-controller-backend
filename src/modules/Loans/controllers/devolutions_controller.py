from src.modules.Loans.services.showStudentsWithLoan import showStudentsWithLoan
from src.modules.Loans.services.showStudentLoans import showStudentLoans

from src.infra.errors.app_error import AppError


def read_students():
    return showStudentsWithLoan.execute()

def read_loans_of_student(ra):
    return showStudentLoans.execute(ra)