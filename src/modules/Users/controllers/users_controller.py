from src.modules.Users.services.createUserService import createUserService
from src.modules.Users.services.showUserService import showUserService
from src.modules.Users.services.updateUserService import updateUserService
from src.modules.Users.services.disableUserService import disableUserService

from src.utils.formValidator import FormValidator
from src.infra.errors.app_error import AppError

def create(obj):
    isValid = FormValidator.isValid(
        'username',
        'email',
        'password',
        'phone',
        'level',
        data=obj)
    if not isValid:
        return AppError(message="missing fields", statusCode=401).error()
    return createUserService.execute(obj)

def read(user_id):
    return showUserService.execute(user_id)

def update(user_id, obj):
    return updateUserService.execute(user_id=user_id, data=obj)

def disable(user_id):
    return disableUserService.execute(user_id)