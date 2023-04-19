from __main__ import app

from src.modules.Books.models.Book import Book
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
from app import db
import json
from sqlalchemy import func, and_

class ShowOneBookService():
    def execute(self, serial):
        book = Book.query.filter_by(serial = serial).first()
        if book is None:
            return {}
        return book.as_dict()

showOneBookService = ShowOneBookService()