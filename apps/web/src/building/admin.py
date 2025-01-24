from src import BuildingModel
from wtforms import StringField
from wtforms.validators import Regexp
from sqladmin import ModelView


class BuildingAdmin(ModelView, model=BuildingModel):
    name = "Здание"
    name_plural = "Здания"
    category = "Здание"
    column_list = [BuildingModel.id, BuildingModel.name,
                   BuildingModel.city, BuildingModel.street,
                   BuildingModel.house_number, BuildingModel.point]
    column_details_exclude_list = [BuildingModel.created_at, BuildingModel.updated_at]
    form_excluded_columns = [BuildingModel.created_at, BuildingModel.updated_at]

    form_overrides = {
        'point': StringField
    }

    form_args = {
        'point': {
            'label': 'Координаты (WKT)',
            'validators': [

                Regexp(
                    r'POINT\(\s*\d+(\.\d+)?\s+\d+(\.\d+)?\s*\)',
                    message="Введите координаты в формате WKT, например: POINT(30 10)"
                )
            ]
        }
    }