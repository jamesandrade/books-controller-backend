from src.modules.Students.services.createStudentService import createStudentService
from src.modules.Students.services.showStudentsService import showStudentsService
from flask import jsonify
from src.utils.formValidator import FormValidator
from src.infra.errors.app_error import AppError

def create(obj):
    isValid = FormValidator.isValid(
        'name',
        'year',
        'team',
        'period',
        data=obj)
    if not isValid:
        return AppError(message="missing fields", statusCode=401).error()
    return createStudentService.execute(obj)
def read():
    return jsonify(showStudentsService.execute())