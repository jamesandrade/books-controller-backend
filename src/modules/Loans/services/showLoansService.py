from __main__ import app

from src.modules.Loans.models.Loan import Loan
from app import db

class ShowLoansService():
    def execute(self):
        loans = Loan.query.order_by(Loan.created_at.desc()).limit(150).all()
        loans_list = []
        for loan in loans:
            loans_list.append(loan.as_dict())
        return loans_list

showLoansService = ShowLoansService()