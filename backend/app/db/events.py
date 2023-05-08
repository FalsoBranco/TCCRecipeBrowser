from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine

from app.config import AppSettings


async def connect_to_db(app: FastAPI, settings: AppSettings) -> None:
    app.state.db = create_async_engine(settings.assembly_database_uri)


async def close_db_connection(app: FastAPI) -> None:
    await app.state.db.dispose()
