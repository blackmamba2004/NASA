from pydantic import BaseModel

from backend.app.components.mixins import FilterMixin


class BaseSchema(BaseModel, FilterMixin):
    pass