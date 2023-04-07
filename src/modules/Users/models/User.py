import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy

from src.infra.database.models import db

class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    level = db.Column(db.Integer, unique=False, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    def __repr__(self):
        return '<User %r>' % self.username

    def as_dict(self):
        res = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        res.pop('password')
        return res