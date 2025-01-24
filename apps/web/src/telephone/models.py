from typing import TYPE_CHECKING
from src.base.base_models.db_models import Base, str_256
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


if TYPE_CHECKING:
    from src import OrganizationModel


class TelephoneModel(Base):
    __tablename__ = 'telephones'

    number: Mapped[str_256] = mapped_column(nullable=False, unique=True)

    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id", ondelete="RESTRICT"))
    organization: Mapped["OrganizationModel"] = relationship(back_populates='telephones')

    def __str__(self) -> str:
        return self.number