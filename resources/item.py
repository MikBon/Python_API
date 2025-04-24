from flask_restful import Resource
from flask import request
from models.item import ItemModel
from db import db

class Item(Resource):
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return {
            "id": item.id,
            "name": item.name,
            "price": item.price,
            "store_id": item.store_id
        }

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted"}

class ItemList(Resource):
    def get(self):
        items = ItemModel.query.all()
        return [{
            "id": i.id,
            "name": i.name,
            "price": i.price,
            "store_id": i.store_id
        } for i in items]

    def post(self):
        data = request.get_json()
        item = ItemModel(
            name=data["name"],
            price=data["price"],
            store_id=data["store_id"]
        )
        db.session.add(item)
        db.session.commit()
        return {
            "id": item.id,
            "name": item.name,
            "price": item.price,
            "store_id": item.store_id
        }, 201
