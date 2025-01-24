from pydantic import BaseModel, field_validator
import geoalchemy2.shape as geoshape
from src.organization.schemas import GetOrganizationDTO


class GetBuildingDTO(BaseModel):
    id: int
    name: str
    city: str
    street: str
    house_number: str
    point: dict

    @field_validator('point', mode='before')
    @classmethod
    def convert_point(cls, v):
        if v is None:
            return None

        shape = geoshape.to_shape(v)

        return {'x': shape.x, 'y': shape.y}


class GetBuildingAndOrganizationDTO(GetBuildingDTO):
    organizations: list[GetOrganizationDTO]