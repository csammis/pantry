"""Schema and object definitions"""

import datetime as dt
from marshmallow import Schema, fields


class UnitSchema(Schema):
    """marshmallow schema for a Unit"""

    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    plural = fields.String()
    created_at = fields.DateTime(load_default=dt.datetime.now())
