from typing import Any, Generic, TypeVar

from backend.app.dto import BaseSchema, Paginator

Entity = TypeVar("Entity")

class Response(BaseSchema, Generic[Entity]):
    paginator: Paginator | None = None
    data: Any = None
