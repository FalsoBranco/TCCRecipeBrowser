from typing import Callable

from fastapi import FastAPI

from app.config import AppSettings
from app.db.events import close_db_connection, connect_to_db


def create_start_handler(app: FastAPI, settings: AppSettings) -> Callable:
    async def start_app() -> None:
        await connect_to_db(app, settings)

    return start_app


def create_stop_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app
