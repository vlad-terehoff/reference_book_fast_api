from src.activity.schemas import GetActivityDTO, GetThirdActivityDTO
from src.base.base_models.dto_models import BaseDto
from src.telephone.schemas import GetTelephoneDTO
from pydantic import Field


class GetOrganizationDTO(BaseDto):
    name: str
    telephones: list[GetTelephoneDTO]
    office_number: str | None
    activities: list[GetActivityDTO] | None = Field(serialization_alias='activities_first_second_rank')
    third_activity: list[GetThirdActivityDTO] | None
