from flask import Response
import json

class AppError:
    def __init__(self, message, statusCode) -> None:
        self.message = message
        self.statusCode = statusCode
    def error(self):
        error = json.dumps({'error': self.message})
        return Response(error, status=self.statusCode, mimetype='application/json')
