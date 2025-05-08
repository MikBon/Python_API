from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

from models.item import ItemModel
from db import db

blp = Blueprint("Items", "items", description="Operations on items")

@blp.route("/item/<int:item_id>")
class Item(MethodView):
    @jwt_required()
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}

    @jwt_required()
    def put(self, item_id):
        from flask import request
        item = ItemModel.query.get_or_404(item_id)
        data = request.get_json()
        item.price = data["price"]
        db.session.commit()
        return item

@blp.route("/item")
class ItemList(MethodView):
    @jwt_required()
    def get(self):
        return ItemModel.query.all()

    @jwt_required()
    def post(self):
        from flask import request
        data = request.get_json()
        item = ItemModel(**data)
        db.session.add(item)
        db.session.commit()
        return item, 201
