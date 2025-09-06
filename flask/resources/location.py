"""Routes and blueprints for storage locations"""

# pylint: disable=missing-class-docstring, missing-function-docstring, import-error

from dataclasses import dataclass, field
import datetime as dt
import uuid
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
    "1": Location("1", "Fridge", "fridge"),
    "2": Location("2", "Freezer", "snowflake", is_freezer=True),
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
            location.name = location_data["name"]
            location.icon = location_data["icon"]
            location.is_freezer = location_data["is_freezer"]
            return location
        except KeyError:
            abort(404)

    def delete(self, location_id):
        try:
            del locations[location_id]
            return {"message": "Location deleted"}
        except KeyError:
            abort(404)


@blp.route("/api/location")
class LocationListEndpoint(MethodView):
    @blp.response(200, LocationSchema(many=True))
    def get(self):
        return locations.values()

    @blp.arguments(LocationSchema)
    @blp.response(201, LocationSchema)
    def post(self, data):
        for _, location in locations.items():
            if location.name == data["name"]:
                abort(400)

        new_id = uuid.uuid4().hex
        location = Location(
            id=new_id,
            name=data["name"],
            icon=data["icon"],
            is_freezer=data["is_freezer"],
        )
        locations[new_id] = location
        return location
