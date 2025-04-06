from typing import Any, Dict, List, Optional

from datetime import datetime

import aiohttp

from backend.app.components import AppLogger
from backend.app.components.utils.pages import paginate
from backend.app.dto import (
    BaseSchema, MarsPhotoListDTO, MartianSolFilters, MissionFilters
)
from backend.app.enums import RoverNameEnum



class NasaAPIService:
    BASE_URL = "https://api.nasa.gov"

    def __init__(
        self, logger: AppLogger, base_url: str, api_key: str
    ):
        self._logger = logger
        self._logger.activate(__class__.__name__)

        self.base_url = base_url
        self.api_key = api_key
        
    def build_query_string(
        self, schema: BaseSchema
    ) -> str:
        query_string = schema.query_string
        api_key = f"&api_key={self.api_key}"
        if query_string is None:
            return api_key
        return query_string + api_key

    async def get_photos_with_info(
        self, martian_sol_filters: MartianSolFilters
    ) -> MarsPhotoListDTO:
        query_str = self.build_query_string(martian_sol_filters)

        async with aiohttp.ClientSession() as client:
            response = await client.get(
                f"{self.BASE_URL}/mars-photos/api/v1/"\
                f"rovers/curiosity/photos?{query_str}"
            )
            if response.status == 200:
                return await response.json()
            
            error_text = await response.text()
            print(error_text)
            self._logger.error(
                "Ошибка обращения к API Nasa", exc_info=None
            )
            return { 
                "photos": []
            }
    
    async def get_mission_manifest_info(
        self, 
        rover_name: RoverNameEnum,
    ):
        async with aiohttp.ClientSession() as client:
            response = await client.get(
                f"{self.BASE_URL}/mars-photos/api/v1/"\
                f"manifests/{rover_name}?api_key={self.api_key}"
            )
            return await response.json()

    async def filter_by(self, mission_filters: MissionFilters):
        filters = mission_filters.model_dump()
        page = filters.pop("page")
        size = filters.pop("size")

        data = await self.get_mission_manifest_info(filters["rover_name"])
        
        sol_activities = data["photo_manifest"]["photos"]
        
        sol_activities = await self.filters(sol_activities, filters)
        
        sol_activities, paginator = paginate(sol_activities, page, size)

        data["photo_manifest"]["sol_activities"] = sol_activities
        del data["photo_manifest"]["photos"]
        
        return {
            "paginator": paginator,
            "data": data
        } 

    async def filters(
        self, 
        sol_activities: List[Dict[str, Any]], 
        filters: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        sol_activities = self.filter_by_sol(
            sol_activities, 
            filters.get("sol_from"), 
            filters.get("sol_to")
        )
        
        sol_activities = self.filter_by_date(
            sol_activities, 
            filters.get("earth_date_from"), 
            filters.get("earth_date_to")
        )
        
        sol_activities = self.filter_by_photos(
            sol_activities, 
            filters.get("min_total_photo"), 
            filters.get("max_total_photo")
        )
        
        sol_activities = self.filter_by_cameras(
            sol_activities, 
            filters.get("cameras")
        )
        
        return sol_activities

    def filter_by_sol(
        self,
        sol_activities: List[Dict[str, Any]],
        sol_from: Optional[int],
        sol_to: Optional[int]
    ) -> List[Dict[str, Any]]:
        if sol_from:
            sol_activities = [
                sol_activity for sol_activity in sol_activities
                if sol_activity["sol"] >= sol_from
            ]
        if sol_to:
            sol_activities = [
                sol_activity for sol_activity in sol_activities
                if sol_activity["sol"] <= sol_to
            ]
        return sol_activities

    def filter_by_date(
        self,
        sol_activities: List[Dict[str, Any]],
        earth_date_from: Optional[str],
        earth_date_to: Optional[str]
    ) -> List[Dict[str, Any]]:
        if earth_date_from:
            sol_activities = [
                sol_activity for sol_activity in sol_activities
                if datetime.strptime(sol_activity["earth_date"], "%Y-%m-%d").date() >= earth_date_from
            ]
        if earth_date_to:
            sol_activities = [
                sol_activity for sol_activity in sol_activities
                if datetime.strptime(sol_activity["earth_date"], "%Y-%m-%d").date() <= earth_date_to
            ]
        return sol_activities

    def filter_by_photos(
        self,
        sol_activities: List[Dict[str, Any]],
        min_total_photo: Optional[int],
        max_total_photo: Optional[int]
    ) -> List[Dict[str, Any]]:
        if min_total_photo:
            sol_activities = [
                sol_activity for sol_activity in sol_activities
                if sol_activity["total_photos"] >= min_total_photo
            ]
        if max_total_photo:
            sol_activities = [
                sol_activity for sol_activity in sol_activities
                if sol_activity["total_photos"] <= max_total_photo
            ]
        return sol_activities

    def filter_by_cameras(
        self,
        sol_activities: List[Dict[str, Any]],
        cameras: Optional[List[str]]
    ) -> List[Dict[str, Any]]:
        if cameras:
            return [
                sol_activity for sol_activity in sol_activities
                if any(cam.name in sol_activity["cameras"] for cam in cameras)
            ]
        return sol_activities