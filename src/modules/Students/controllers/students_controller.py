from src.modules.Students.services.createStudentService import createStudentService
from src.modules.Students.services.showStudentsService import showStudentsService
from flask import jsonify
from src.utils.formValidator import FormValidator
from src.infra.errors.app_error import AppError

def create(user_id, obj):
    obj["user_id"] = user_id
    isValid = FormValidator.isValid(
        'name',
        'terms',
        'team',
        'period',
        'user_id',
        data=obj)
    if not isValid:
        return AppError(message="missing fields", statusCode=401).error()
    return createStudentService.execute(obj)
def read():
    return jsonify(showStudentsService.execute())