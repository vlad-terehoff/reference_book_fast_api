from sqladmin import ModelView
from src.user.models import UserModel


class UserAdmin(ModelView, model=UserModel):
    name = "Пользователь"
    name_plural = "Пользователи"
    category = "Пользователи"
    column_list = [UserModel.id, UserModel.login]
    form_columns = [UserModel.login, UserModel.static_token]
    column_details_list = [UserModel.login, UserModel.static_token]