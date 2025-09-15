"""sqlalchemy model of an Item"""

# pylint: disable=missing-class-docstring, too-few-public-methods, import-error, unnecessary-lambda


import datetime as dt
import uuid
from db import Base, Id
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ItemModel(Base):
    __tablename__ = "item"

    id: Mapped[Id] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str]

    location_id: Mapped[Id] = mapped_column(ForeignKey("location.id"))
    location: Mapped["LocationModel"] = relationship(
        uselist=False, back_populates="items"
    )

    unit_id: Mapped[Id | None] = mapped_column(ForeignKey("unit.id"))
    unit_quantity: Mapped[float | None]

    created_at: Mapped[dt.datetime] = mapped_column(
        nullable=False, default=lambda: dt.datetime.now()
    )
    modified_at: Mapped[dt.datetime | None]
    moved_at: Mapped[dt.datetime | None]
