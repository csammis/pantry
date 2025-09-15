"""sqlalchemy model of a Unit"""

# pylint: disable=missing-class-docstring, too-few-public-methods, import-error, unnecessary-lambda

import datetime as dt
import uuid
from db import Base, Id
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column


class UnitModel(Base):
    __tablename__ = "unit"
    __table_args__ = (UniqueConstraint("name"),)

    id: Mapped[Id] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str]
    plural: Mapped[str | None]
    created_at: Mapped[dt.datetime] = mapped_column(default=lambda: dt.datetime.now())
