from typing import AsyncGenerator, Callable

from fastapi import Depends
from fastapi.requests import Request
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

from app.db.repositories.base import BaseRepository


def _get_database_engine(request: Request) -> AsyncEngine:
    return request.app.state.db


async def _get_session_from_engine(
    engine: AsyncEngine = Depends(_get_database_engine),
) -> AsyncGenerator[AsyncSession, None]:
    _async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(engine)
    async with _async_session() as session:
        yield session


def get_repository(
    repo_type: type[BaseRepository],
) -> Callable[[AsyncSession], BaseRepository]:
    def _get_repo(
        session: None | AsyncSession = Depends(_get_session_from_engine),
    ) -> BaseRepository:
        return repo_type(session=session)

    return _get_repo
