import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
from src.infra.database.models import db

class Registration(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student = db.Column(UUID(as_uuid=True), db.ForeignKey('student.id'), nullable=False)
    year = db.Column(db.Integer, nullable=False, default=datetime.now().year)
    team = db.Column(db.String(120), unique=False, nullable=False)
    period = db.Column(db.String(250), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('America/Sao_Paulo')), nullable=False)
    updated_at = db.Column(db.DateTime , nullable=True)
    created_by = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    updated_by = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=True)
    def __repr__(self):
        return '<Registration %r>' % self.id

    def as_dict(self):
        res = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return res
