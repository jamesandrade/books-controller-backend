from __main__ import app

from flask import request, jsonify
from flask_jwt_extended import jwt_required

from src.infra.jwt.level_user import level_user
from src.modules.Users.controllers import users_controller, login_controller

ROUTE = "/users"
@app.route(ROUTE, methods=['POST'])
def create_user():
    return users_controller.create(request.json)

@app.route(ROUTE+"/<user_id>", methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@level_user()
def users(user_id):
    if request.method == 'GET':
        return users_controller.read(user_id)
    elif request.method == 'PUT':
        return users_controller.update(user_id, obj=request.json)
    elif request.method == 'DELETE':
        return users_controller.disable(user_id)

@app.route(ROUTE+"/login", methods=['POST'])
def login():
    return login_controller.login(request.json)
