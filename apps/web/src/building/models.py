from typing import TYPE_CHECKING
from src.base.base_models.db_models import Base, str_256
from sqlalchemy.orm import Mapped, mapped_column, relationship
from geoalchemy2 import Geometry

if TYPE_CHECKING:
    from src import OrganizationModel


class BuildingModel(Base):
    __tablename__ = 'buildings'

    name: Mapped[str_256] = mapped_column(nullable=False, unique=True)
    city: Mapped[str_256] = mapped_column(nullable=False)
    street: Mapped[str_256] = mapped_column(nullable=False)
    house_number: Mapped[str_256] = mapped_column(nullable=False)

    point: Mapped[Geometry] = mapped_column(Geometry('POINT', srid=4326))

    organizations: Mapped[list["OrganizationModel"]] = relationship(back_populates='building')

    def __str__(self) -> str:
        return self.name
