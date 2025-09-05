"""Routes and blueprints for storage locations"""

# pylint: disable=missing-class-docstring, missing-function-docstring, import-error

from dataclasses import dataclass, field
import datetime as dt
from flask_smorest import Blueprint
from schemas import LocationSchema
from flask import abort
from flask.views import MethodView

blp = Blueprint(
    "locations", __name__, "Storage locations (fridge, freezer, pantry, etc.)"
)


@dataclass
class Location:
    """ORM representation of a storage location"""

    id: str
    name: str
    icon: str
    created_at: dt.datetime = field(default_factory=dt.datetime.now)
    is_freezer: bool = field(default=False)


locations: dict[str, Location] = {
    "1": Location("1", "Fridge", "mdi:fridge"),
    "2": Location("2", "Freezer", "mdi:snowflake"),
}


@blp.route("/api/location/<string:location_id>")
class LocationEndpoint(MethodView):
    @blp.response(200, LocationSchema)
    def get(self, location_id):
        try:
            return locations[location_id]
        except KeyError:
            abort(404)

    @blp.arguments(LocationSchema)
    @blp.response(200, LocationSchema)
    def put(self, location_data, location_id):
        try:
            location = locations[location_id]
            location |= location_data
        except KeyError:
            abort(404)


@blp.route("/api/location")
class LocationListEndpoint(MethodView):
    @blp.response(200, LocationSchema(many=True))
    def get(self):
        return locations.values()
