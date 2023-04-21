from __main__ import app
from app import db
from src.modules.Loans.models.Loan import Loan
from datetime import datetime
from collections import defaultdict
from operator import itemgetter

class TopFiveService():
    def execute(self, start_date, end_date):
        results = Loan.query.filter(
            Loan.returned==True,
            Loan.reason_devolution==2,
            Loan.returned_at.between(start_date, end_date)
        )
        if results is None:
            return []

        loans = []
        for result in results:
            loans.append(result.as_dict())

        books_read = defaultdict(int)
        for loan in loans:
            ra = loan["student"]["ra"]
            books_read[ra] += 1

        books_read = sorted(books_read.items(), key=itemgetter(1), reverse=True)

        top_alunos = []
        for i, (ra, books) in enumerate(books_read):
            if i == 5:
                break
            student = {}
            for loan in loans:
                if loan["student"]["ra"] == ra:
                    student = loan["student"]
            top_alunos.append({
                "position": i + 1,
                "student": student,
                "label": f"{student.get('name', None)} {student.get('registration').get('team').replace('º ', 'º').replace('ª ', 'ª')}",
                "value": int(books),
                "read_books": int(books)
            })
        return top_alunos
topFiveService = TopFiveService()