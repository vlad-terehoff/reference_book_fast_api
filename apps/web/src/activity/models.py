from typing import TYPE_CHECKING
from src.base.base_models.db_models import Base, str_256
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Index


if TYPE_CHECKING:
    from src import OrganizationModel


class ActivityModel(Base):
    __tablename__ = 'activity'
    __table_args__ = (
        Index('idx_name_activity', 'name'),
    )

    name: Mapped[str_256] = mapped_column(nullable=False, unique=True)

    organizations: Mapped[list['OrganizationModel']] = relationship('OrganizationModel',
                                                                    secondary='organization_activity_association',
                                                                    back_populates='activities')

    main_activities_id: Mapped[int | None] = mapped_column(ForeignKey("activity.id", ondelete="RESTRICT"),
                                                           nullable=True)
    main_activities: Mapped["ActivityModel"] = relationship(back_populates='sub_activities',
                                                            remote_side='ActivityModel.id')

    sub_activities: Mapped[list['ActivityModel']] = relationship(back_populates='main_activities')

    third_activity: Mapped[list['ThirdActivityModel']] = relationship(secondary='activity_third_activity_association',
                                                                      back_populates='main_activities')

    def __str__(self) -> str:
        return self.name


class ThirdActivityModel(Base):
    __tablename__ = 'third_activity'
    __table_args__ = (
        Index('idx_name_third_activity', 'name'),
    )

    name: Mapped[str_256] = mapped_column(nullable=False, unique=True)

    organizations: Mapped[list['OrganizationModel']] = relationship(secondary='organization_third_activity_association',
                                                                    back_populates='third_activity')

    main_activities: Mapped[list["ActivityModel"]] = relationship(secondary='activity_third_activity_association',
                                                                  back_populates='third_activity')

    def __str__(self) -> str:
        return self.name



