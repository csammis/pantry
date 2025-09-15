"""Routes and blueprints for stored items"""

# pylint: disable=missing-class-docstring, missing-function-docstring, import-error

import datetime as dt
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from schemas import ItemSchema, PlainItemSchema
from db import db
from models.item import ItemModel
from flask.views import MethodView

blp = Blueprint("items", __name__, "Items stored in Pantry")


@blp.route("/api/item/<string:item_id>")
class ItemEndpoint(MethodView):
    @classmethod
    def get_or_404(cls, item_id: str) -> ItemModel:
        """Get the specified Item or abort with a HTTP 404 error"""
        item = db.session.query(ItemModel).filter(ItemModel.id == item_id)
        if not item:
            abort(404)
        return item

    @blp.response(200, ItemSchema)
    def get(self, item_id):
        return ItemEndpoint.get_or_404(item_id)

    @blp.arguments(PlainItemSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        try:
            item = ItemEndpoint.get_or_404(item_id)
            item.name = item_data["name"]
            if item.location_id != item_data["location_id"]:
                item.location_id = item_data["location_id"]
                item.moved_at = dt.datetime.now()
            item.unit_id = (
                None if "unit_id" not in item_data else item_data["item_data"]
            )
            item.unit_quantity = (
                None if "unit_quantity" not in item_data else item_data["unit_quantity"]
            )
            item.modified_at = dt.datetime.now()

            db.session.add(item)
            db.session.commit()
            return item
        except IntegrityError:
            abort(400)

    def delete(self, item_id):
        try:
            item = ItemEndpoint.get_or_404(item_id)
            db.session.delete(item)
            db.session.commit()
            return {"message": "Item deleted"}, 200
        except IntegrityError:
            abort(404)


@blp.route("/api/item")
class ItemListEndpoint(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return db.session.query(ItemModel)

    @blp.arguments(PlainItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, data):
        print(data)
        try:
            item = ItemModel(**data)
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(400)
        except SQLAlchemyError as sae:
            print(sae)
            abort(500)
        return item
