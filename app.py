from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from src.infra.jwt.jwtConfig import JwtConfig
from src.infra.server.server import startserver
from src.infra.database.DatabaseConfig import DatabaseConfig
from src.infra.database.models import db

app = startserver()
DatabaseConfig.config(app)
db.init_app(app)
JwtConfig.init(app)
jwt = JWTManager(app)
import src.modules.models
migrate = Migrate(app, db)

if __name__ == "__main__":
    import src.infra.routes.startroutes
    app.run(host='0.0.0.0', port=5000, debug=True)