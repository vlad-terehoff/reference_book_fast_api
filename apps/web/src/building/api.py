from typing import List
from fastapi import APIRouter, Depends
from src.auth.user_auth import checking_validity_token
from src.base.db_settings.session import ISession
from src.building.schemas import GetBuildingDTO
from src.building.service import building_service
from src.organization.schemas import GetOrganizationDTO


buildings_router = APIRouter(prefix="/buildings",
                               tags=["BUILDINGS"],
                               dependencies=[Depends(checking_validity_token)])


@buildings_router.get("/", response_model=List[GetBuildingDTO])
async def get_all_buildings(session: ISession):
    '''Для получения всех зданий для того что бы получить id объекта и сделать запрос на получение организации'''
    return await building_service.get_all(session=session)


@buildings_router.get("/get_all_organization/{id}", response_model=List[GetOrganizationDTO])
async def get_all_organization_by_buildings_id(id: int, session: ISession):
    '''Получение всех организаций в здание'''
    return await building_service.get_all_organization(session=session, id=id)