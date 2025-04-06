from dishka import Provider

from .app_logger import AppLoggerProvider
from .nasa import NasaAPIProvider
from .settings import SettingsProvider


def provider_list() -> list[Provider]:
    return [
        AppLoggerProvider(),
        NasaAPIProvider(),
        SettingsProvider(),
    ]
