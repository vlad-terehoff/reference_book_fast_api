from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from src import UserModel
from src.base.db_settings.session import ISession
from sqlalchemy import select


http_bearer = HTTPBearer()


async def validate_user_by_token(token, session):
    stmt = select(UserModel).filter_by(static_token=token)
    raw = await session.execute(stmt)

    return raw.scalar_one_or_none()


async def checking_validity_token(
        session: ISession,
        credentials: HTTPAuthorizationCredentials = Depends(http_bearer)):
    token = credentials.credentials
    await validate_user_by_token(token, session)