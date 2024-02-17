import logging

from pydantic_settings import SettingsConfigDict

logger = logging.getLogger()


class Settings:
    """Instance which imports and provides data from the .env file."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    host_address: str = "localhost"
    DB_HOST: str = str()
    DB_NAME: str = str()
    DB_USER: str = str()
    DB_PASSWORD: str = str()
    DB_PORT: str = str()
    DB_SSL_MODE: str = "prefer"
