"""SQLAlchemy models for locations"""

# pylint: disable=missing-class-docstring, too-few-public-methods, import-error

import uuid
from db import db
from sqlalchemy import String, DateTime, Column, Boolean


class LocationModel(db.Model):
    __tablename__ = "location"

    id: Column = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Column = Column(String(80), unique=True, nullable=False)
    icon: Column = Column(String(80), nullable=True)
    is_freezer: Column = Column(Boolean, default=False)
    created_at: Column = Column(DateTime)
