from typing import TYPE_CHECKING
from src.base.base_models.db_models import Base, str_256
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Index

if TYPE_CHECKING:
    from src import TelephoneModel, ActivityModel, ThirdActivityModel, BuildingModel


class OrganizationModel(Base):
    __tablename__ = 'organizations'
    __table_args__ = (
        Index('idx_building_id', 'building_id'),
        Index('idx_name', 'name'),
    )

    name: Mapped[str_256] = mapped_column(nullable=False, unique=True)

    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id", ondelete="RESTRICT"))
    building: Mapped["BuildingModel"] = relationship("BuildingModel", back_populates='organizations')

    telephones: Mapped[list["TelephoneModel"]] = relationship(back_populates='organization', lazy='selectin')

    office_number: Mapped[str_256 | None] = mapped_column(nullable=True)

    activities: Mapped[list['ActivityModel']] = relationship('ActivityModel',
                                                             secondary='organization_activity_association',
                                                             back_populates='organizations',
                                                             lazy='selectin')

    third_activity: Mapped[list['ThirdActivityModel']] = relationship(
        secondary='organization_third_activity_association',
        back_populates='organizations',
        lazy='selectin')

    def __str__(self) -> str:
        return self.name



