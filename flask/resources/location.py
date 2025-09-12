"""Routes and blueprints for storage locations"""

# pylint: disable=missing-class-docstring, missing-function-docstring, import-error

from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from db import db
from schemas import LocationSchema
from models.location import LocationModel
from flask.views import MethodView

blp = Blueprint(
    "locations", __name__, "Storage locations (fridge, freezer, pantry, etc.)"
)


@blp.route("/api/location/<string:location_id>")
class LocationEndpoint(MethodView):
    @classmethod
    def get_or_404(cls, location_id: str) -> LocationModel:
        """Get the specified Location or abort with a HTTP 404 error"""
        location: LocationModel = (
            db.session.query(LocationModel)
            .filter(LocationModel.id == location_id)
            .first()
        )
        if not location:
            abort(404)
        return location

    @blp.response(200, LocationSchema)
    def get(self, location_id):
        return LocationEndpoint.get_or_404(location_id)

    @blp.arguments(LocationSchema)
    @blp.response(200, LocationSchema)
    def put(self, location_data, location_id):
        try:
            location = LocationEndpoint.get_or_404(location_id)
            location.name = location_data["name"]
            location.icon = location_data["icon"]
            location.is_freezer = location_data["is_freezer"]
            db.session.add(location)
            db.session.commit()
            return location
        except IntegrityError:
            abort(400, message="Duplicate names are not allowed")

    def delete(self, location_id):
        try:
            location = LocationEndpoint.get_or_404(location_id)
            db.session.delete(location)
            db.session.commit()
            return {"message": "Location deleted"}, 200
        except IntegrityError:
            abort(400, message="Location is in use by other records")


@blp.route("/api/location")
class LocationListEndpoint(MethodView):
    @blp.response(200, LocationSchema(many=True))
    def get(self):
        return db.session.query(LocationModel)

    @blp.arguments(LocationSchema)
    @blp.response(201, LocationSchema)
    def post(self, data):
        location = LocationModel(**data)
        try:
            db.session.add(location)
            db.session.commit()
            return location
        except IntegrityError:
            abort(400, message="Duplicate names are not allowed")
        except SQLAlchemyError as sae:
            print(sae)
            abort(500)
