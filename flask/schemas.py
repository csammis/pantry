"""Schema and object definitions"""

import datetime as dt
from marshmallow import Schema, fields


class UnitSchema(Schema):
    """marshmallow schema for a Unit"""

    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    plural = fields.String()
    created_at = fields.DateTime(dump_only=True, load_default=dt.datetime.now())


class PlainLocationSchema(Schema):
    """marshmallow schema for a Location"""

    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    icon = fields.String()
    created_at = fields.DateTime(dump_only=True, load_default=dt.datetime.now())
    is_freezer = fields.Boolean(load_default=False)


class PlainItemSchema(Schema):
    """marshmallow schema for an Item"""

    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    location_id = fields.String(required=True)
    unit_id = fields.String(allow_none=True)
    unit_quantity = fields.Float(allow_none=True)
    created_at = fields.DateTime(dump_only=True, load_default=dt.datetime.now())
    modified_at = fields.DateTime(dump_only=True)
    moved_at = fields.DateTime(dump_only=True)


class LocationSchema(Schema):
    """marshmallow schema for a Location with a nested list of Items"""

    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    icon = fields.String()
    created_at = fields.DateTime(dump_only=True, load_default=dt.datetime.now())
    is_freezer = fields.Boolean(load_default=False)
    items = fields.List(fields.Nested(PlainItemSchema))


class ItemSchema(Schema):
    """marshmallow schema for an Item with a nested Location and Unit"""

    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    location = fields.Nested(PlainLocationSchema)
    unit = fields.Nested(UnitSchema, allow_none=True)
    unit_quantity = fields.Float(allow_none=True)
    created_at = fields.DateTime(dump_only=True, load_default=dt.datetime.now())
    modified_at = fields.DateTime(dump_only=True)
    moved_at = fields.DateTime(dump_only=True)
