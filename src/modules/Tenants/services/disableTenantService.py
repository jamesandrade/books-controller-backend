from __main__ import app

from src.infra.errors.app_error import AppError
from src.modules.Tenants.models.Tenant import Tenant
from app import db

class DisableTenantService():
    def execute(self, tenant_id):
        tenant = Tenant.query.filter_by(id=tenant_id).first()
        if not tenant:
            return AppError(message="Tenant does not exists", statusCode=404).error()
        try:
            tenant.allowed = False
            db.session.commit()
        except:
            db.session.rollback()
            return AppError(message="Default Error", statusCode=500).error()

        return tenant.as_dict()

disableTenantService = DisableTenantService()