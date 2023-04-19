from __main__ import app

from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.modules.Loans.controllers import loans_controller
from src.modules.Loans.controllers import devolutions_controller

ROUTE = "/loans"
@app.route(ROUTE, methods=['GET', 'POST', 'PUT'])
@jwt_required()
def loans():
    if request.method == 'POST':
        user_id = get_jwt_identity()
        return loans_controller.create(user_id=user_id, obj=request.json)
    elif request.method == 'GET':
        return loans_controller.read()
    elif request.method == 'PUT':
        user_id = get_jwt_identity()
        return loans_controller.update(user_id=user_id, obj=request.json)

@app.route(f"{ROUTE}/students", methods=['GET'])
@jwt_required()
def students_with_loan():
    if request.method == 'GET':
        return devolutions_controller.read_students()

@app.route(f"{ROUTE}/students/<ra>", methods=['GET'])
@jwt_required()
def loans_of_student(ra):
    if request.method == 'GET':
        return devolutions_controller.read_loans_of_student(ra)
