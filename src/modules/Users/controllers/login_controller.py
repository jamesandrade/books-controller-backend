from src.utils.formValidator import FormValidator
from src.infra.errors.app_error import AppError
from src.modules.Users.services.loginService import loginService

def login(obj):
    isValid = FormValidator.isValid(
        'email',
        'password',
        data=obj)
    if not isValid:
        return AppError(message="missing fields", statusCode=401).error()
    return loginService.execute(obj)