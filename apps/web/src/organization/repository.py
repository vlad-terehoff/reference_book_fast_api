from src import OrganizationModel, ActivityModel, ThirdActivityModel, BuildingModel
from src.base.db_settings.session import ISession
from sqlalchemy import select, and_, func
from sqlalchemy.orm import selectinload
from src.exceptions.exceptions import exec_catch


class OrganizationRepository:

    async def get_all_by_id_building(self, id: int, session: ISession):
        stmt = select(OrganizationModel).where(OrganizationModel.building_id == id)
        raw = await session.execute(stmt)

        return raw.scalars().all()

    @exec_catch
    async def get_by_id(self, id: int, session: ISession):
        stmt = select(OrganizationModel).where(OrganizationModel.id == id)
        raw = await session.execute(stmt)

        return raw.scalar_one()

    @exec_catch
    async def get_by_name(self, name: str, session: ISession):
        stmt = select(OrganizationModel).where(OrganizationModel.name == name)
        raw = await session.execute(stmt)

        return raw.scalar_one()

    async def filter_by_activities_name(self, name: str, session: ISession):
        stmt = select(OrganizationModel).join(OrganizationModel.activities).where(ActivityModel.name == name)
        raw = await session.execute(stmt)

        return raw.scalars().all()

    async def filter_by_third_activities_name(self, name: str, session: ISession):
        stmt = select(OrganizationModel).join(OrganizationModel.third_activity).where(ThirdActivityModel.name == name)
        raw = await session.execute(stmt)

        return raw.scalars().all()

    async def filter_by_activities_and_third_activities_name(self, name_first: str, name_third: str, session: ISession):
        stmt = (select(OrganizationModel)
        .join(OrganizationModel.third_activity)
        .join(OrganizationModel.activities)
        .where(and_(
            ActivityModel.name == name_first,
            ThirdActivityModel.name == name_third
        )))
        raw = await session.execute(stmt)

        return raw.scalars().all()

    async def find_organization_in_radius(self,
                                          center_lon: float,
                                          center_lat: float,
                                          radius_km: float,
                                          session: ISession):

        stmt = select(BuildingModel).options(selectinload(BuildingModel.organizations)).where(
            func.ST_DWithin(
                BuildingModel.point,
                func.ST_GeographyFromText(f'POINT({center_lon} {center_lat})'),
                radius_km * 1000
            )
        )

        raw = await session.execute(stmt)

        return raw.scalars().all()

    async def find_organization_in_rectangle(self,
                                         min_lon: float,
                                         min_lat: float,
                                         max_lon: float,
                                         max_lat: float,
                                         session: ISession):

        stmt = select(BuildingModel).options(selectinload(BuildingModel.organizations)).where(
            func.ST_Intersects(
                BuildingModel.point,
                func.ST_MakeEnvelope(min_lon, min_lat, max_lon, max_lat, 4326)
            )
        )

        raw = await session.execute(stmt)

        return raw.scalars().all()


organization_repository = OrganizationRepository()
