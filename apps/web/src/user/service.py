from src.user.repository import UserRepository, user_repository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def get_for_auth(self, session, user: str):
        result = await self.repository.get_for_auth(session=session, user=user)
        return result


user_service = UserService(user_repository)