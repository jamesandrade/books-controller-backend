from src.modules.Students.services.createStudentService import createStudentService
from src.modules.Students.services.showStudentsService import showStudentsService
from src.modules.Students.services.showOneStudentService import showOneStudentService
from src.modules.Students.services.updateStudentService import updateStudentService

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

def readOne(ra):
    return showOneStudentService.execute(ra)

def update(user_id, ra, obj):
    obj["user_id"] = user_id
    obj["ra"] = ra
    isValid = FormValidator.isValid(
        'user_id',
        'ra',
        data=obj)
    if not isValid:
        return AppError(message="missing fields", statusCode=401).error()
    return updateStudentService.execute(obj)