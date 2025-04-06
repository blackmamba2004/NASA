from backend.app.dto import BaseSchema


class Paginator(BaseSchema):
    page: int
    total: int
    has_prev: bool
    has_next: bool
