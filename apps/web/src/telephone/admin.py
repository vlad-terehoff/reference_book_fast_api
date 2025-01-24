from sqladmin import ModelView
from src.telephone.models import TelephoneModel


class TelephoneAdmin(ModelView, model=TelephoneModel):
    name = "Телефон"
    name_plural = "Телефоны"
    category = "Телефоны"
    column_list = [TelephoneModel.id, TelephoneModel.number, TelephoneModel.organization]
    column_details_exclude_list = [TelephoneModel.created_at, TelephoneModel.updated_at]
    form_excluded_columns = [TelephoneModel.created_at, TelephoneModel.updated_at]