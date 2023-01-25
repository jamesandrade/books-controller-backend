from __main__ import app

from src.modules.Tenants.models.Tenant import Tenant
from app import db

class ShowTenantService():
    def execute(self, data):
        tenant = Tenant.query.filter_by(id=data).first()
        return tenant.as_dict() if tenant else []

showTenantService = ShowTenantService()