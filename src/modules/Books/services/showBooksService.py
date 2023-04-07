from __main__ import app

from src.modules.Books.models.Book import Book
from src.modules.Loans.models.Loan import Loan
from app import db

class ShowBooksService():
    def execute(self):
        books = Book.query.all()
        books_list = []
        for book in books:
            newBook = book.as_dict()
            newBook["is_loaned"] = Loan.book_is_loaned(newBook["id"])
            books_list.append(newBook) 
        return books_list

showBooksService = ShowBooksService()