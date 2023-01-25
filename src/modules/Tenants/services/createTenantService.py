from __main__ import app
from sqlalchemy import exc

from src.infra.errors.app_error import AppError
from src.modules.Tenants.models.Tenant import Tenant
from app import db

class CreateTenantService():
    def execute(self, data):
        data["corporate_name"] = data["corporate_name"].upper()
        data["fantasy_name"] = data["fantasy_name"].upper()
        data["owner"] = data["owner"].title()
        try:
            newTenant = Tenant(**data)
            db.session.add(newTenant)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            return AppError(message="Integrity Error", statusCode=409).error()
        except:
            db.session.rollback()
            return AppError(message="Default Error", statusCode=500).error()

        return newTenant.as_dict()

createTenantService = CreateTenantService()