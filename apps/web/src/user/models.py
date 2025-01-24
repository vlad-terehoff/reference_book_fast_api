from src.base.base_models.db_models import Base, str_256
from sqlalchemy.orm import Mapped, mapped_column


class UserModel(Base):
    __tablename__ = 'users'

    login: Mapped[str_256] = mapped_column(nullable=False, unique=True)
    static_token: Mapped[str] = mapped_column(nullable=False)

    def __str__(self) -> str:
        return self.login
