import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
from flask_sqlalchemy import SQLAlchemy
from src.infra.database.models import db

class Student(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(120), unique=False, nullable=False)
    ra = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(120), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=False, nullable=True)
    phone = db.Column(db.String(120), unique=False, nullable=True)
    terms = db.Column(db.Boolean, default=False, nullable=False)
    disabled = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('America/Sao_Paulo')), nullable=False)
    updated_at = db.Column(db.DateTime , nullable=True)
    created_by = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    updated_by = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=True)
    def __repr__(self):
        return '<Student %r>' % self.name

    def as_dict(self):
        res = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return res

    def get_student_by_id(student_id):
        student = Student.query.get(student_id)
        return student