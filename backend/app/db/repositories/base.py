from sqlalchemy.ext.asyncio.session import AsyncSession


class BaseRepository(object):
    def __init__(self, session: AsyncSession) -> None:
        self._session: AsyncSession = session

    @property
    def session(self) -> AsyncSession:
        return self._session
