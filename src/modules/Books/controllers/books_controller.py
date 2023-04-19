from src.modules.Books.services.createBookService import createBookService
from src.modules.Books.services.showBooksService import showBooksService
from src.modules.Books.services.showOneBookService import showOneBookService
from src.modules.Books.services.updateBookService import updateBookService

from flask import jsonify
from src.utils.formValidator import FormValidator
from src.infra.errors.app_error import AppError

def create(user_id, obj):
    obj["user_id"] = user_id
    isValid = FormValidator.isValid(
        'title',
        'serial',
        data=obj)
    if not isValid:
        return AppError(message="missing fields", statusCode=401).error()
    return createBookService.execute(obj)
def read():
    return jsonify(showBooksService.execute())
def readOne(serial):
    return showOneBookService.execute(serial)
def update(user_id, obj):
    obj["user_id"] = user_id
    return updateBookService.execute(obj)