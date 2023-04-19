import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy

from src.infra.database.models import db
from datetime import datetime
import pytz
class Book(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(120), unique=False, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    serial = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('America/Sao_Paulo')), nullable=False)
    updated_at = db.Column(db.DateTime , nullable=True)
    created_by = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    updated_by = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=True)
    def __repr__(self):
        return '<Book %r>' % self.title

    def as_dict(self):
        res = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return res

    def get_book_by_id(book_id):
        book = Book.query.get(book_id)
        return book