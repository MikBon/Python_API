from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

from models.tag import TagModel
from db import db

blp = Blueprint("Tags", "tags", description="Operations on tags")

@blp.route("/tag/<int:tag_id>")
class Tag(MethodView):
    @jwt_required()
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag

    @jwt_required()
    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        db.session.delete(tag)
        db.session.commit()
        return {"message": "Tag deleted."}

@blp.route("/tag")
class TagList(MethodView):
    @jwt_required()
    def get(self):
        return TagModel.query.all()

    @jwt_required()
    def post(self):
        from flask import request
        data = request.get_json()
        tag = TagModel(**data)
        db.session.add(tag)
        db.session.commit()
        return tag, 201
