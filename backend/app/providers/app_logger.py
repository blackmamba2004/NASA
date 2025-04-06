from dishka import Provider, provide, Scope

from backend.app.components import AppLogger
from backend.app.settings import AppSettings


class AppLoggerProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_app_logger(self, app_settings: AppSettings) -> AppLogger:
        return AppLogger(
            app_settings.PROJECT_NAME, 
            app_settings.LOG_LEVEL
        )