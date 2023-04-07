import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy

from src.infra.database.models import db

class Student(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(120), unique=False, nullable=False)
    year = db.Column(db.String(120), unique=False, nullable=True)
    team = db.Column(db.String(120), unique=False, nullable=True)
    period = db.Column(db.String(250), unique=False, nullable=False)
    def __repr__(self):
        return '<Student %r>' % self.name

    def as_dict(self):
        res = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return res

    def get_student_by_id(student_id):
        student = Student.query.get(student_id)
        return student