from __main__ import app

from src.infra.errors.app_error import AppError
from src.modules.Tenants.models.Tenant import Tenant
from app import db

class UpdateTenantService():
    def execute(self, tenant_id, data):
        tenant = Tenant.query.filter_by(id=tenant_id)
        if not tenant.first():
            return AppError(message="Tenant does not exists", statusCode=404).error()
        if "corporate_name" in data:
            data["corporate_name"] = data["corporate_name"].upper()
        if "fantasy_name" in data:
            data["fantasy_name"] = data["fantasy_name"].upper()
        if "owner" in data:
            data["owner"] = data["owner"].title()
        try:
            tenant.update(dict(data))
            db.session.commit()
        except:
            db.session.rollback()
            return AppError(message="Default Error", statusCode=500).error()

        updateddata = tenant.first()
        return updateddata.as_dict()

updateTenantService = UpdateTenantService()