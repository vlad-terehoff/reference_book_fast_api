from src.base.base_models.db_models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, UniqueConstraint


class OrganizationActivityAssociationModel(Base):
    __tablename__ = 'organization_activity_association'
    __table_args__ = (
        UniqueConstraint('organization_id',
                         'activity_id',
                         name='ind_unique_organization_activity'),
    )

    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
    activity_id: Mapped[int] = mapped_column(ForeignKey("activity.id"))


class ActivityThirdActivityAssociationModel(Base):
    __tablename__ = 'activity_third_activity_association'
    __table_args__ = (
        UniqueConstraint('main_activities_id',
                         'third_activity_id',
                         name='ind_unique_activity_third_activity'),
    )

    main_activities_id: Mapped[int] = mapped_column(ForeignKey("activity.id"))
    third_activity_id: Mapped[int] = mapped_column(ForeignKey("third_activity.id"))


class OrganizationThirdActivityAssociationModel(Base):
    __tablename__ = 'organization_third_activity_association'
    __table_args__ = (
        UniqueConstraint('organization_id',
                         'third_activity_id',
                         name='ind_unique_organization_third_activity'),
    )

    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
    third_activity_id: Mapped[int] = mapped_column(ForeignKey("third_activity.id"))