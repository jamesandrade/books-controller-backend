from __main__ import app

from flask import request
from flask_jwt_extended import jwt_required

from src.modules.Students.controllers import students_controller

ROUTE = "/students"
@app.route(ROUTE, methods=['GET','POST'])
@jwt_required()
def students():
    if request.method == 'POST':
        return students_controller.create(request.json)
    elif request.method == 'GET':
        return students_controller.read()