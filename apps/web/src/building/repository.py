from src import BuildingModel
from src.base.db_settings.session import ISession
from sqlalchemy import select


class BuildingRepository:

    async def get_all(self, session: ISession):
        stmt = select(BuildingModel)
        raw = await session.execute(stmt)

        return raw.scalars().all()


building_repository = BuildingRepository()
