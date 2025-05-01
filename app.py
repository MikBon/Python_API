from flask import Flask
from flask_restful import Api
from db import db
from resources.store import Store
from resources.tag import Tag

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)
    api.add_resource(Store, "/store", "/store/<int:store_id>")
    api.add_resource(Tag, "/tag", "/tag/<int:tag_id>")

    return app
