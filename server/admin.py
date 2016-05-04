from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from models import CrowdfundingProject

admin = Admin(app, name="microblog", template_mode="bootstrap3")
admin.add_view(ModelView(CrowdfundingProject, db.session))