from flask_restful import Resource
from flask import request
from models.tag import TagModel
from models.store import StoreModel
from db import db

class Tag(Resource):
    def post(self):
        data = request.get_json()
        store = StoreModel.query.get_or_404(data["store_id"])
        tag = TagModel(name=data["name"], store=store)
        db.session.add(tag)
        db.session.commit()
        return {"id": tag.id, "name": tag.name, "store_id": tag.store_id}, 201

    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return {
            "id": tag.id,
            "name": tag.name,
            "store": {"id": tag.store.id, "name": tag.store.name}
        }
