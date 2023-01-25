from src.modules.Tenants.services.createTenantService import createTenantService
from src.modules.Tenants.services.showTenantService import showTenantService
from src.modules.Tenants.services.updateTenantService import updateTenantService
from src.modules.Tenants.services.disableTenantService import disableTenantService

from src.utils.formValidator import FormValidator
from src.infra.errors.app_error import AppError
def create(obj):
    isValid = FormValidator.isValid(
        'corporate_name',
        'fantasy_name',
        'cpnj',
        'email',
        'phone',
        'owner',
        'cpf_owner',
        data=obj)
    if not isValid:
        return AppError(message="missing fields", statusCode=401).error()
    return createTenantService.execute(obj)
def read(tenant_id):
    return showTenantService.execute(tenant_id)
def update(tenant_id, obj):
    return updateTenantService.execute(tenant_id=tenant_id, data=obj)
def disable(tenant_id):
    return disableTenantService.execute(tenant_id)