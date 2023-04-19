from __main__ import app
import os
from sqlalchemy import exc
from datetime import datetime
import pytz
from src.modules.Loans.models.Loan import Loan
from src.infra.errors.app_error import AppError
from app import db

class UpdateLoanService():
    def execute(self, data):
        try:
            date_now = datetime.now(pytz.timezone('America/Sao_Paulo'))
            data['updated_at'] = date_now
            data['updated_by'] = data["user_id"]
            data.pop('user_id')
            id_register = data.pop('id', None)
            if id_register is None:
                return []

            register = Loan.query.filter_by(id=id_register).first()
            if register is None:
                return []

            for key, value in data.items():
                setattr(register, key, value)

            db.session.commit()
            return register.as_dict()

        except Exception as e:
            db.session.rollback()
            raise e

updateLoanService = UpdateLoanService()