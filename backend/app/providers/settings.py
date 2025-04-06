from dishka import Provider, provide, Scope

from backend.app.settings import AppSettings


class SettingsProvider(Provider):
    scope = Scope.APP

    @provide
    def get_app_settings(self) -> AppSettings:
        return AppSettings()