"""SQLAlchemy models for units"""

# pylint: disable=missing-class-docstring, too-few-public-methods, import-error

import uuid
from db import db
from sqlalchemy import String, DateTime, Column


class UnitModel(db.Model):
    __tablename__ = "unit"

    id: Column = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Column = Column(String(80), unique=True, nullable=False)
    plural: Column = Column(String(80), nullable=True)
    created_at: Column = Column(DateTime)
