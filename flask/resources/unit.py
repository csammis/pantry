"""Routes and blueprints for quantity units"""

# pylint: disable=missing-class-docstring, missing-function-docstring, import-error

from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from db import db
from schemas import UnitSchema
from models import UnitModel
from flask.views import MethodView

blp = Blueprint("units", __name__, "Units of quantity (cups, pints, loaves, etc.)")


@blp.route("/api/unit/<string:unit_id>")
class UnitEndpoint(MethodView):
    @blp.response(200, UnitSchema)
    def get(self, unit_id):
        return UnitModel.query.get_or_404(unit_id)

    @blp.arguments(UnitSchema)
    @blp.response(200, UnitSchema)
    def put(self, unit_data, unit_id):
        try:
            unit = UnitModel.query.get_or_404(unit_id)
            unit.name = unit_data["name"]
            unit.plural = unit_data["plural"]
            db.session.add(unit)
            db.session.commit()
            return unit
        except IntegrityError:
            abort(400, "Duplicate names are not allowed")

    def delete(self, unit_id):
        try:
            unit = UnitModel.query.get_or_404(unit_id)
            db.session.delete(unit)
            db.session.commit()
            return {"message": "Unit deleted"}, 200
        except IntegrityError:
            abort(400, "Unit is in use by other records")


@blp.route("/api/unit")
class UnitListEndpoint(MethodView):
    @blp.response(200, UnitSchema(many=True))
    def get(self):
        return UnitModel.query.all()

    @blp.arguments(UnitSchema)
    @blp.response(201, UnitSchema)
    def post(self, data):
        unit = UnitModel(**data)
        try:
            db.session.add(unit)
            db.session.commit()
            return unit
        except IntegrityError:
            abort(400, message="Duplicate names are not allowed")
        except SQLAlchemyError as sae:
            print(sae)
            abort(500)
