from src.base.db_settings.session import ISession
from src.building.repository import BuildingRepository, building_repository
from src.organization.service import organization_service


class BuildingService:
    def __init__(self, repository: BuildingRepository):
        self.repository = repository

    async def get_all(self, session: ISession):
        result = await self.repository.get_all(session=session)
        return result


    async def get_all_organization(self, id: int, session: ISession):
        result = await organization_service.get_all_by_id_building(session=session, id=id)
        return result


building_service = BuildingService(building_repository)