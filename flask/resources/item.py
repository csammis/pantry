"""Routes and blueprints for stored items"""

# pylint: disable=missing-class-docstring, missing-function-docstring, import-error

from dataclasses import dataclass, field
import datetime as dt
import uuid
from flask_smorest import Blueprint
from schemas import ItemSchema
from flask import abort
from flask.views import MethodView

blp = Blueprint("items", __name__, "Items stored in Pantry")


@dataclass
class Item:
    """ORM representation of a stored item"""

    id: str
    name: str
    location_id: str
    unit_id: str | None = field(default=None)
    unit_quantity: float | None = field(default=None)
    created_at: dt.datetime = field(default_factory=dt.datetime.now)
    modified_at: dt.datetime = field(default_factory=dt.datetime.now)
    moved_at: dt.datetime = field(default_factory=dt.datetime.now)


items: dict[str, Item] = {
    "1": Item("1", "Ice Cream", "2", "1", "3"),
    "2": Item("2", "Water", "1"),
    "3": Item("3", "Frozen Pizza", "2", None, "2"),
}


@blp.route("/api/item/<string:item_id>")
class ItemEndpoint(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404)

    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        try:
            item = items[item_id]
            item.name = item_data["name"]
            item.location_id = item_data["location_id"]
            item.unit_id = (
                None if "unit_id" not in item_data else item_data["item_data"]
            )
            item.unit_quantity = (
                None if "unit_quantity" not in item_data else item_data["unit_quantity"]
            )
            item.modified_at = dt.datetime.now()
            return item
        except KeyError:
            abort(404)

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "item deleted"}
        except KeyError:
            abort(404)


@blp.route("/api/item")
class ItemListEndpoint(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, data):
        for _, item in items.items():
            if item.name == data["name"]:
                abort(400)

        new_id = uuid.uuid4().hex
        item = Item(id=new_id, name=data["name"], location_id=data["location_id"])
        item.unit_id = None if "unit_id" not in data else data["item_data"]
        item.unit_quantity = (
            None if "unit_quantity" not in data else data["unit_quantity"]
        )
        items[new_id] = item
        return item
