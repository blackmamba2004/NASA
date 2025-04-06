from typing import Annotated

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, Query


from backend.app.dto import (
    MarsPhotoListDTO, 
    MartianSolFilters, 
    MissionFilters,
    Response
)

from backend.app.service import NasaAPIService


router = APIRouter(route_class=DishkaRoute)


@router.get(
    "/nasa/photos",
    response_model=Response[MarsPhotoListDTO]
)
async def get_photos(
    martian_sol_filters: Annotated[MartianSolFilters, Query()],
    nasa_api_service: FromDishka[NasaAPIService],
):
    return await nasa_api_service.get_photos_with_info(martian_sol_filters)

@router.get(
    "/nasa/mission"
)
async def get_mission(
    nasa_api_service: FromDishka[NasaAPIService],
    mission_filters: Annotated[MissionFilters, Query()]
):
    return await nasa_api_service.filter_by(mission_filters)
