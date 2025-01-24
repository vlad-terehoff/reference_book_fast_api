from sqladmin import ModelView
from src import ActivityModel, ThirdActivityModel


class ActivityModelAdmin(ModelView, model=ActivityModel):
    name = "Активность первого и второго порядка"
    name_plural = "Активность первого и второго порядка"
    category = "Активность первого и второго порядка"
    column_list = [ActivityModel.id, ActivityModel.name,
                   ActivityModel.organizations, ActivityModel.main_activities]
    column_details_exclude_list = [ActivityModel.created_at, ActivityModel.updated_at]
    form_excluded_columns = [ActivityModel.created_at, ActivityModel.updated_at]


class ThirdActivityModelAdmin(ModelView, model=ThirdActivityModel):
    name = "Активность третьего порядка"
    name_plural = "Активность третьего порядка"
    category = "Активность третьего порядка"
    column_list = [ThirdActivityModel.id, ThirdActivityModel.name,
                   ActivityModel.organizations, ActivityModel.main_activities]
    column_details_exclude_list = [ThirdActivityModel.created_at, ThirdActivityModel.updated_at]
    form_excluded_columns = [ThirdActivityModel.created_at, ThirdActivityModel.updated_at]