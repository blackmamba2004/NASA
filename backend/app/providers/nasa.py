from dishka import Provider, provide, Scope

from backend.app.components import AppLogger
from backend.app.service import NasaAPIService
from backend.app.settings import AppSettings


class NasaAPIProvider(Provider):
    scope = Scope.REQUEST
    
    @provide
    def get_nasa_api_service(
        self, app_logger: AppLogger, app_settings: AppSettings
    ) -> NasaAPIService:
        return NasaAPIService(
            app_logger, 
            app_settings.NASA_BASE_URL, 
            app_settings.NASA_API_KEY
        )
