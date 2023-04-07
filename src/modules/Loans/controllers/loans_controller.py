from src.modules.Loans.services.createLoanService import createLoanService
from src.modules.Loans.services.showLoansService import showLoansService

from flask import jsonify
from src.utils.formValidator import FormValidator
from src.infra.errors.app_error import AppError

def create(obj):
    isValid = FormValidator.isValid(
        'student',
        'book',
        'loan',
        data=obj)
    if not isValid:
        return AppError(message="missing fields", statusCode=401).error()
    return createLoanService.execute(obj)
def read():
    return showLoansService.execute()
