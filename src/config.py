from functools import lru_cache
from logging import INFO
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.resolve()

class Settings(BaseSettings):

    TITLE: str = "MatchGraft AI"
    VERSION: str = "0.1.0"
    TIMEZONE: str = "UTC"
    DESCRIPTION: str = "API documentation for backend application of MatchGraft AI"
    DEBUG: bool = True

    SERVER_HOST: str = "127.0.0.1"
    SERVER_PORT: int = 8000
    SERVER_WORKERS: int = 2
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""
    SECRET_KEY: str = "MatchGraft-Secret-Key"

    IS_ALLOWED_CREDENTIALS: bool = True
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://match-graft.vercel.app"
    ]
    ALLOWED_METHODS: list[str] = ["*"]
    ALLOWED_HEADERS: list[str] = ["*"]

    LOGGING_LEVEL: int = INFO
    LOGGERS: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    STORAGE_DIR: str = str(BASE_DIR / Path("storage/"))

    STORAGE_JSON: dict[str, str] = {
        "patients": str(BASE_DIR / Path("storage/patients.json")),
        "donors": str(BASE_DIR / Path("storage/donors.json")),
        "cases": str(BASE_DIR / Path("storage/cases.json")),
    }

    model_config = SettingsConfigDict(case_sensitive=True, validate_assignment=True)


    @property
    def set_backend_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` class' attributes with the custom values defined in `BackendBaseSettings`.
        """
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
