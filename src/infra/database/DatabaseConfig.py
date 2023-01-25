import os

class DatabaseConfig():
    def config(app):
        app.config['SQLALCHEMY_DATABASE_URI'] = f"{os.environ['POSTGRES_HOST']}://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSW']}@postgresql:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DATABASE']}"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False