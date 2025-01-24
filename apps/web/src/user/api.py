from fastapi import APIRouter, Depends
from src.auth.user_auth import checking_validity_token
from src.base.db_settings.session import ISession
from src.user.schemas import GetUserDTO
from src.user.service import user_service


user_router = APIRouter(prefix="/user_login", tags=["User_Login"])


@user_router.get("/{user}/", response_model=GetUserDTO)
async def get_for_auth(user: str, session: ISession):
    '''Аунтификация для получения статического токена'''
    return await user_service.get_for_auth(user=user, session=session)

