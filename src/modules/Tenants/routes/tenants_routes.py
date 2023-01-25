from __main__ import app

from flask import request, jsonify
from flask_jwt_extended import jwt_required

from src.infra.jwt.level_user import level_user
from src.modules.Tenants.controllers import tenants_controller

ROUTE = "/tenants"
@app.route(ROUTE, methods=['POST'])
def create_tenant():
    return tenants_controller.create(request.json)

@app.route(ROUTE+"/<tenant_id>", methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@level_user()
def tenants(tenant_id):
    if request.method == 'GET':
        return tenants_controller.read(tenant_id)
    elif request.method == 'PUT':
        return tenants_controller.update(tenant_id, obj=request.json)
    elif request.method == 'DELETE':
        return tenants_controller.disable(tenant_id)


