from typing import List
from fastapi import APIRouter, Depends, Query
from src.auth.user_auth import checking_validity_token
from src.base.db_settings.session import ISession
from src.building.schemas import GetBuildingAndOrganizationDTO
from src.organization.schemas import GetOrganizationDTO
from src.organization.service import organization_service

organization_router = APIRouter(prefix="/organization",
                                tags=["ORGANIZATION"],
                                dependencies=[Depends(checking_validity_token)])


@organization_router.get("/get_by_id/{id}", response_model=GetOrganizationDTO)
async def get_by_id(id: int, session: ISession):
    '''Для получения организации по id'''
    return await organization_service.get_by_id(session=session, id=id)


@organization_router.get("/get_by_name/{name}", response_model=GetOrganizationDTO)
async def get_by_name(name: str, session: ISession):
    '''Получение организации по имени'''
    return await organization_service.get_by_name(session=session, name=name)


@organization_router.get("/get_by_names_activities", response_model=List[GetOrganizationDTO])
async def get_by_names_activities(session: ISession,
                                  name_first: str | None = Query(None),
                                  name_third: str | None = Query(None)
                      ):
    '''Для фильтрации организаций по названию активности первого - второго или по названию третьего порядка'''
    return await organization_service.get_by_names_activities(session=session,
                                                              name_first=name_first,
                                                              name_third=name_third)


@organization_router.get("/find_in_radius", response_model=List[GetBuildingAndOrganizationDTO])
async def find_organization_in_radius(session: ISession,
                                      center_lon: float = Query(),
                                      center_lat: float = Query(),
                                      radius_km: float = Query()):

    '''Для фильтрации организаций и зданий по радиусу от точки поиска'''

    return await organization_service.find_organization_in_radius(session=session,
                                                                  center_lon=center_lon,
                                                                  center_lat=center_lat,
                                                                  radius_km=radius_km)


@organization_router.get("/find_in_rectangle", response_model=List[GetBuildingAndOrganizationDTO])
async def find_objects_in_rectangle(session: ISession,
                                      center_lon: float = Query(),
                                      center_lat: float = Query(),
                                      width_km: float = Query(),
                                      height_km: float = Query()):

    '''Для фильтрации организаций и зданий по прямоугольнику от точки поиска'''

    return await organization_service.find_objects_in_rectangle(session=session,
                                                                center_lon=center_lon,
                                                                center_lat=center_lat,
                                                                width_km=width_km,
                                                                height_km=height_km)