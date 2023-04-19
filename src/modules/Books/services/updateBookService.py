from __main__ import app
import os
from sqlalchemy import exc
from datetime import datetime
import pytz
import re

from src.modules.Books.models.Book import Book
from src.infra.errors.app_error import AppError
from app import db

class UpdateBookService():

    def execute(self, data):
        try:
            date_now = datetime.now(pytz.timezone('America/Sao_Paulo'))
            book = {}
            book.update(data)
            book['updated_at'] = date_now
            book['updated_by'] = data["user_id"]
            book.pop("user_id")
            updatedBook = Book.query.filter_by(id = data["id"])
            if updatedBook.first() is None:
                return {}
            updatedBook.update(book)
            db.session.commit()
            return updatedBook.first().as_dict()
        except exc.IntegrityError:
            db.session.rollback()
            return AppError(message="Integrity Error", statusCode=409).error()
        except:
            db.session.rollback()
            return AppError(message="Default Error", statusCode=500).error()

updateBookService = UpdateBookService()