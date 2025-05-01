from flask_restful import Resource
from flask import request
from models.store import StoreModel
from db import db

class Store(Resource):
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return {
            "id": store.id,
            "name": store.name,
            "tags": [{"id": tag.id, "name": tag.name} for tag in store.tags]
        }

    def post(self):
        data = request.get_json()
        store = StoreModel(name=data["name"])
        db.session.add(store)
        db.session.commit()
        return {"id": store.id, "name": store.name}, 201
