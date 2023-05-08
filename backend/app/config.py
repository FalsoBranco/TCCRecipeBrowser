from functools import lru_cache
from typing import Any

from dynaconf import Dynaconf, LazySettings
from pydantic import BaseSettings, SecretStr
from sqlalchemy.engine import URL


class AppSettings(BaseSettings):
    TITLE: str | None
    DEBUG: bool | None
    VERSION: str | None

    API_PREFIX: str | None
    DOCS_URL: str | None

    OPENAPI_PREFIX: str | None
    OPENAPI_URL: str | None
    REDOC_URL: str | None

    SECRET_KEY: SecretStr | None

    # Database

    JWT_TOKEN_PREFIX: str = "Token"

    ALLOWED_HOSTS: list[str] | None

    DB_HOST: str | None
    DB_USER: str | None
    DB_PASSWORD: str | None
    DB_NAME: str | None
    DB_SCHEMA: str | None
    DB_PORT: int | None

    @property
    def assembly_database_uri(self) -> str:
        url: URL = URL.create(
            drivername=self.DB_SCHEMA,
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.DB_NAME,
        )

        return url.render_as_string()

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        return {
            "debug": self.DEBUG,
            "docs_url": self.DOCS_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "title": self.TITLE,
            "version": self.VERSION,
        }


configuration: LazySettings = Dynaconf(
    envvar_prefix=False,
    environments=True,
    load_dotenv=True,
    settings_files=[
        "app/core/settings/settings.toml",
        "app/core/settings/.secrets.toml",
    ],
)


@lru_cache
def get_app_settings() -> AppSettings:
    settings: AppSettings = AppSettings()

    settings_properties: list[str] = [
        properties.upper() for properties in settings.dict().keys()
    ]

    configuration.populate_obj(settings, keys=settings_properties)
    return settings
