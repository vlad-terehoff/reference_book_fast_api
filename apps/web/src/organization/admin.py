from sqladmin import ModelView
from src.organization.models import OrganizationModel


class OrganizationAdmin(ModelView, model=OrganizationModel):
    name = "Организация"
    name_plural = "Организации"
    category = "Организации"
    column_list = [OrganizationModel.id, OrganizationModel.name,
                   OrganizationModel.building, OrganizationModel.telephones, OrganizationModel.office_number]
    column_details_exclude_list = [OrganizationModel.created_at, OrganizationModel.updated_at]
    form_excluded_columns = [OrganizationModel.created_at, OrganizationModel.updated_at]