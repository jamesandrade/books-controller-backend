from __main__ import app

from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.modules.Reports.controllers import reports_controller

ROUTE = "/reports"

@app.route(f"{ROUTE}/topfive", methods=['GET'])
@jwt_required()
def topFive():
    if request.method == 'GET':
        start_date = request.args.get('start_date', None)
        end_date = request.args.get('end_date', None)
        if start_date is None or end_date is None:
            return []
        return reports_controller.topFive(start_date, end_date)

@app.route(f"{ROUTE}/all", methods=['GET'])
@jwt_required()
def topAll():
    if request.method == 'GET':
        start_date = request.args.get('start_date', None)
        end_date = request.args.get('end_date', None)
        if start_date is None or end_date is None:
            return []
        return reports_controller.topAll(start_date, end_date)
