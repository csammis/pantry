"""
Flask REST server for pantry
"""

import os
from resources.unit import blp as UnitBlueprint
from resources.location import blp as LocationBlueprint
from db import db
from flask_smorest import Api
from flask import Flask


def create_app(db_url: str = None) -> Flask:
    """App factory method"""
    app = Flask(__name__)
    app.config["API_TITLE"] = "pantry"
    app.config["API_VERSION"] = "0.0.1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )
    api = Api(app)

    api.register_blueprint(UnitBlueprint)
    api.register_blueprint(LocationBlueprint)

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", "sqlite:///data.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
