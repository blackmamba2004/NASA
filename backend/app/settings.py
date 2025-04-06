from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    PROJECT_NAME: str

    LOG_LEVEL: str = "DEBUG"

    NASA_BASE_URL: str
    NASA_API_KEY: str

    model_config = SettingsConfigDict(env_file='.env')

