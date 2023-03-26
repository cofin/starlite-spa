"""Application ORM configuration."""

from __future__ import annotations

from typing import Any, TypeVar

from starlite.contrib.sqlalchemy.base import AuditColumns, meta
from starlite.contrib.sqlalchemy.base import Base as DatabaseModel

__all__ = ["DatabaseModel", "meta", "model_from_dict", "AuditColumns"]

DatabaseModelT = TypeVar("DatabaseModelT", bound="DatabaseModel")


def model_from_dict(model: type[DatabaseModelT], data: dict[str, Any]) -> DatabaseModelT:
    """Return ORM Object from Dictionary."""
    obj_in = {}
    if model.__table__ is not None:
        for column in model.__table__.columns:
            if column.name in data:
                obj_in.update({column.name: data.get(column.name)})
    return model(**obj_in)
