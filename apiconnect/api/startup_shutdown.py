from fastapi import FastAPI

from apiconnect.settings import Settings
from apiconnect.utils.database.connector import DBconnector


def create_events_startup_shutdown(app: FastAPI, env_settings: Settings) -> None:
    """Inject startup and shutdown components into given FastAPI application."""

    @app.on_event("startup")
    async def setup_connection_ingest_data() -> None:
        """Autonomous fx to insert data in rec engine database."""
        app.state.db_connector = DBconnector(env_settings)

    @app.on_event("shutdown")
    async def teardown_connection() -> None:
        await app.state.db_connector.dispose_engine()
