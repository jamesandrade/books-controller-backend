from src.modules.Books.services.createBookService import createBookService
from src.modules.Books.services.showBooksService import showBooksService
from flask import jsonify
from src.utils.formValidator import FormValidator
from src.infra.errors.app_error import AppError

def create(obj):
    isValid = FormValidator.isValid(
        'title',
        'serial',
        data=obj)
    if not isValid:
        return AppError(message="missing fields", statusCode=401).error()
    return createBookService.execute(obj)
def read():
    return jsonify(showBooksService.execute())