from fastapi import FastAPI
from sqladmin import Admin
from src.activity.admin import ActivityModelAdmin, ThirdActivityModelAdmin
from src.base.db_settings.db_helper import db_helper
from src.auth.admin_auth import authentication_backend
from src.building.admin import BuildingAdmin
from src.building.api import buildings_router
from src.organization.admin import OrganizationAdmin
from src.organization.api import organization_router
from src.telephone.admin import TelephoneAdmin
from src.user.admin import UserAdmin
from src.user.api import user_router


app = FastAPI(root_path="/api")

admin = Admin(app=app, engine=db_helper.engine, session_maker=db_helper.session_factory,
              authentication_backend=authentication_backend)

app.include_router(user_router)
app.include_router(buildings_router)
app.include_router(organization_router)


admin.add_view(UserAdmin)
admin.add_view(TelephoneAdmin)
admin.add_view(OrganizationAdmin)
admin.add_view(BuildingAdmin)
admin.add_view(ActivityModelAdmin)
admin.add_view(ThirdActivityModelAdmin)

