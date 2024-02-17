import logging

import uvicorn
from fastapi import FastAPI

from apiconnect.settings import Settings
import apiconnect.api.endpoints as endpoint

logger = logging.getLogger()


def create_app(env_set=Settings()) -> FastAPI:
    """Create fastapi application (ASGI) based on given settings."""
    app = FastAPI(title="APIConnect")

    app.include_router(endpoint.router)

    return app


def main():
    """Start API server."""
    env_set = Settings()

    uvicorn.run(
        "apiconnect.main:create_app",
        factory=True,
        host=env_set.host_address,
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
