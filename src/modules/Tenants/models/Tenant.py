from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import uuid
from src.infra.database.models import db

class Tenant(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    corporate_name = db.Column(db.String(80), unique=False, nullable=False)
    fantasy_name = db.Column(db.String(80), unique=False, nullable=False)
    cpnj = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=False, nullable=False)
    owner =  db.Column(db.String(120), unique=False, nullable=False)
    cpf_owner = db.Column(db.String(120), unique=False, nullable=False)
    coordinate_x = db.Column(db.String(80), unique=False, nullable=True)
    coordinate_y = db.Column(db.String(80), unique=False, nullable=True)
    head_office =  db.Column(db.Boolean, unique=False, nullable=False, default=True)
    allowed =  db.Column(db.Boolean, unique=False, nullable=False, default=True)
    created_at = db.Column(db.DateTime, unique=False, nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return '<Tenant %r>' % self.cnpj

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}