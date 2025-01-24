from src import UserModel
from src.base.db_settings.session import ISession
from src.exceptions.exceptions import exec_catch
from sqlalchemy import select


class UserRepository:

    @exec_catch
    async def get_for_auth(self, user: str, session: ISession):
        stmt = select(UserModel).filter_by(login=user)
        raw = await session.execute(stmt)

        return raw.scalar_one()


user_repository = UserRepository()
