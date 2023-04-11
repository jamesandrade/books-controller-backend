from __main__ import app

from flask import request
from flask_jwt_extended import jwt_required

from src.modules.Loans.controllers import loans_controller

ROUTE = "/loans"
@app.route(ROUTE, methods=['GET', 'POST', 'PUT'])
@jwt_required()
def loans():
    if request.method == 'POST':
        return loans_controller.create(request.json)
    elif request.method == 'GET':
        return loans_controller.read()
    elif request.method == 'PUT':
        return loans_controller.update(request.json)