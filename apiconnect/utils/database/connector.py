import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from rec_engine_aircraft_library import settings

logger = logging.getLogger()


class DBconnector:
    """Sets up asynchronous connection to a database base on given environment settings."""

    __db_url: str
    __engine: AsyncEngine
    async_session_factory: sessionmaker[AsyncSession]  # type: ignore

    def __init__(self, env_settings: settings.RecEngineAircraftSettings):
        """Initialize asynchronous engine, s.t. asynchronous may be created using the async_session_factory."""
        self.__db_url = (
            f"postgresql+asyncpg://{env_settings.DB_USER}:{env_settings.DB_PASSWORD}"
            + f"@{env_settings.DB_HOST}:{env_settings.DB_PORT}/{env_settings.DB_NAME}"
        )
        self.__engine = create_async_engine(self.__db_url, echo=True)
        self.async_session_factory = sessionmaker(
            autocommit=False, autoflush=False, bind=self.__engine, class_=AsyncSession
        )

    async def dispose_engine(self):
        """Close and delete created engine."""
        await self.__engine.dispose()

    def get_engine(self) -> AsyncEngine:
        """Get private variable __engine."""
        return self.__engine

    async def connection_check(self) -> bool:
        """Check the connection with the database."""
        try:
            async with self.__engine.begin() as conn:
                await conn.execute(select(1))  # type: ignore
            logger.info("Database connection is alive.")
            return True
        except Exception as e:
            logger.error(f"Error during database health check: {e}")
            return False
