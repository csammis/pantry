"""Routes and blueprints for quantity units"""

# pylint: disable=missing-class-docstring, missing-function-docstring, import-error

from dataclasses import dataclass, field
import datetime as dt
from flask_smorest import Blueprint
from schemas import UnitSchema
from flask import abort
from flask.views import MethodView

blp = Blueprint("units", __name__, "Units of quantity (cups, pints, loaves, etc.)")


@dataclass
class Unit:
    """ORM representation of a unit of quantity (cup, pint, loaf)"""

    id: str
    name: str
    plural: str
    created_at: dt.datetime = field(default_factory=dt.datetime.now)


units: dict[str, Unit] = {
    "1": Unit("1", "cup", "cups"),
    "2": Unit("2", "pint", "pints"),
    "3": Unit("3", "loaf", "loaves"),
}


@blp.route("/api/unit/<string:unit_id>")
class UnitEndpoint(MethodView):
    @blp.response(200, UnitSchema)
    def get(self, unit_id):
        try:
            return units[unit_id]
        except KeyError:
            abort(404)

    @blp.arguments(UnitSchema)
    @blp.response(200, UnitSchema)
    def put(self, unit_data, unit_id):
        try:
            unit = units[unit_id]
            unit |= unit_data
        except KeyError:
            abort(404)


@blp.route("/api/unit")
class UnitListEndpoint(MethodView):
    @blp.response(200, UnitSchema(many=True))
    def get(self):
        return units.values()
