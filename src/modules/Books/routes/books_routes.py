from __main__ import app

from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.modules.Books.controllers import books_controller

ROUTE = "/books"
@app.route(ROUTE, methods=['GET','POST', 'PUT'])
@jwt_required()
def books():
    if request.method == 'POST':
        user_id = get_jwt_identity()
        return books_controller.create(user_id=user_id, obj=request.json)
    elif request.method == 'GET':
        return books_controller.read()
    elif request.method == 'PUT':
        user_id = get_jwt_identity()
        return books_controller.update(user_id=user_id, obj=request.json)

@app.route(f"{ROUTE}/<serial>", methods=['GET'])
@jwt_required()
def specific_book(serial):
    if request.method == 'GET':
        return books_controller.readOne(serial=serial)
