# pylint: disable=missing-class-docstring, too-few-public-methods, import-error

import datetime as dt
from typing import List
import uuid
from db import Base, Id
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship


class LocationModel(Base):
    __tablename__ = "location"
    __table_args__ = (UniqueConstraint("name"),)

    id: Mapped[Id] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str]
    icon: Mapped[str | None]
    is_freezer: Mapped[bool]
    created_at: Mapped[dt.datetime] = mapped_column(default=lambda: dt.datetime.now())

    items: Mapped[List["ItemModel"]] = relationship(
        back_populates="location", lazy="dynamic"
    )
