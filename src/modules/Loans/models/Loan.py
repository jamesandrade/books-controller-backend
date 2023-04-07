import uuid
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime
from src.infra.database.models import db
from src.modules.Students.models.Student import Student
from src.modules.Books.models.Book import Book

class Loan(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student = db.Column(UUID(as_uuid=True), db.ForeignKey('student.id'), nullable=False)
    book = db.Column(UUID(as_uuid=True), db.ForeignKey('book.id'), nullable=False)
    loan = db.Column(db.Date, nullable=False, default=datetime.utcnow().date())
    returned_at = db.Column(db.Date, nullable=True)
    returned = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id

    def as_dict(self):
        res = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        res["student"] = Student.get_student_by_id(self.student).as_dict()
        res["book"] = Book.get_book_by_id(self.book).as_dict()
        return res

    def book_is_loaned(book_id):
        book = Loan.query.filter_by(
            book = book_id,
            returned = False
        ).first()
        if book:
            return True
        return False
