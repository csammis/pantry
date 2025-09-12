"""Database connector"""

from typing import NewType
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase

Id = NewType("IdColumn", str)


class Base(DeclarativeBase):
    """DeclarativeBase class for ORM models"""

    type_annotation_map = {str: String(80), Id: String(36)}


db = SQLAlchemy()
