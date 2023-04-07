from __main__ import app

from flask import request
from flask_jwt_extended import jwt_required

from src.modules.Books.controllers import books_controller

ROUTE = "/books"
@app.route(ROUTE, methods=['GET','POST'])
@jwt_required()
def books():
    if request.method == 'POST':
        return books_controller.create(request.json)
    elif request.method == 'GET':
        return books_controller.read()