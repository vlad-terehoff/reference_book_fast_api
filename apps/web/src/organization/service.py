from src.base.db_settings.session import ISession
from src.organization.repository import OrganizationRepository, organization_repository
from src.organization.utils import calculate_rectangle_bounds


class OrganizationService:
    def __init__(self, repository: OrganizationRepository):
        self.repository = repository

    async def get_all_by_id_building(self, id: int, session: ISession):
        result = await self.repository.get_all_by_id_building(session=session, id=id)
        return result

    async def get_by_id(self, id: int, session: ISession):
        result = await self.repository.get_by_id(session=session, id=id)
        return result

    async def get_by_name(self, name: str, session: ISession):
        result = await self.repository.get_by_name(session=session, name=name)
        return result

    async def get_by_names_activities(self, name_first: str | None, name_third: str | None, session: ISession):

        if name_first and not name_third:
            result = await (self.repository
                            .filter_by_activities_name(session=session,name=name_first))
            return result

        if name_third and not name_first:
            result = await (self.repository
                            .filter_by_third_activities_name(session=session,name=name_third))
            return result

        if name_first and name_third:
            result = await (self.repository
                            .filter_by_activities_and_third_activities_name(session=session,
                                                                            name_first=name_first,
                                                                            name_third=name_third))
            return result

    async def find_organization_in_radius(self,
                                          center_lon: float,
                                          center_lat: float,
                                          radius_km: float,
                                          session: ISession):

        result = await (self.repository
                        .find_organization_in_radius(session=session,
                                                     center_lon=center_lon,
                                                     center_lat=center_lat,
                                                     radius_km=radius_km))
        return result

    async def find_objects_in_rectangle(self,
                                         center_lon: float,
                                         center_lat: float,
                                         width_km: float,
                                         height_km: float,
                                         session: ISession):

        min_lon, min_lat, max_lon, max_lat = await calculate_rectangle_bounds(center_lon=center_lon,
                                                                              center_lat=center_lat,
                                                                              width_km=width_km,
                                                                              height_km=height_km)

        result = await (self.repository
                        .find_organization_in_rectangle(session=session,
                                                        min_lon=min_lon,
                                                        min_lat=min_lat,
                                                        max_lon=max_lon,
                                                        max_lat=max_lat))
        return result


organization_service = OrganizationService(organization_repository)