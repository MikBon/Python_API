from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from db import db

def create_app():
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Tech Store REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "super-secret-key"

    db.init_app(app)
    api = Api(app)
    jwt = JWTManager(app)

    from resources.user import blp as UserBlueprint
    from resources.item import blp as ItemBlueprint
    from resources.store import blp as StoreBlueprint
    from resources.tag import blp as TagBlueprint

    api.register_blueprint(UserBlueprint)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)

    
    with app.app_context():
        from models import user, item, store, tag
        db.create_all()

    return app
