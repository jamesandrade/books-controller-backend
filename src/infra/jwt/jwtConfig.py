import os
class JwtConfig():

    def init(app):
        app.config["JWT_SECRET_KEY"] = os.environ['JWT_SECRET']