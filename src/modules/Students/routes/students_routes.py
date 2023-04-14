from __main__ import app

from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.modules.Students.controllers import students_controller

ROUTE = "/students"
@app.route(ROUTE, methods=['GET','POST'])
@jwt_required()
def students():
    if request.method == 'POST':
        user_id = get_jwt_identity()
        return students_controller.create(user_id=user_id, obj=request.json)
    elif request.method == 'GET':
        return students_controller.read()

@app.route(f"{ROUTE}/<ra>", methods=['GET'])
def specific_student(ra):
    if request.method == 'GET':
        return students_controller.readOne(ra=ra)

