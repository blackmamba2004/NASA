from datetime import date
from typing import Optional

# from fastapi import Query
from pydantic import Field

from backend.app.enums import RoverCameraEnum, RoverNameEnum
from backend.app.dto import BaseSchema


class MarsCameraDTO(BaseSchema):
    id: int
    name: str
    rover_id: int
    full_name: str


class MarsRoverDTO(BaseSchema):
    id: int
    name: str
    landing_date: date
    launch_date: date
    status: str


class MarsPhotoDTO(BaseSchema):
    id: int
    sol: int
    camera: MarsCameraDTO
    img_src: str
    earth_date: date
    rover: MarsRoverDTO


class MarsPhotoListDTO(BaseSchema):
    photos: list[MarsPhotoDTO]


class MartianSolFilters(BaseSchema):

    sol: Optional[int] = Field(None, description="Марсианское вращение или день")
    earth_date: Optional[date] = Field(None, description="Дата на Земле в формате YYYY-MM-DD")
    camera: Optional[RoverCameraEnum] = Field(None, description="Камера, сделавшая снимок")
    page: Optional[int] = Field(1, gt=0, description='Страница пагинации')


class MissionFilters(BaseSchema):
    rover_name: RoverNameEnum = Field(..., description='Имя ровера')
    sol_from: Optional[int] = Field(1, description='Минимальный день на Марсе')
    sol_to: Optional[int] = Field(4500, description='Максимальный день на Марсе')
    earth_date_from: Optional[date] = Field(None, description='Минимальная земная дата в формате YYYY-mm-dd')
    earth_date_to: Optional[date] = Field(None, description='Максимальная земная дата в формате YYYY-mm-dd')
    min_total_photo: Optional[int] = Field(None, description='Минимальное количество фотографий за день')
    max_total_photo: Optional[int] = Field(None, description='Максимальное количество фотографий за день')
    cameras: Optional[list[RoverCameraEnum]] = Field(None, description='Камеры марсохода')
    page: Optional[int] = Field(1, gt=0, description='Страница пагинации')
    size: Optional[int] = Field(30, gt=0, description='Количество элементов на странице')
    