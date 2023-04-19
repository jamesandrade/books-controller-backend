from __main__ import app
import os
from sqlalchemy import exc
from src.modules.Books.models.Book import Book
from src.infra.errors.app_error import AppError
from app import db

class CreateBookService():
    def execute(self, data):
        try:
            data['created_by'] = data["user_id"]
            data.pop("user_id")
            newBook = Book(**data)
            db.session.add(newBook)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            return AppError(message="Integrity Error", statusCode=409).error()
        except:
            db.session.rollback()
            return AppError(message="Default Error", statusCode=500).error()

        return newBook.as_dict()

createBookService = CreateBookService()