from flask_restful import Api

from app import app
from resources import Project, Projects

api = Api(app)

api.add_resource(Projects,'/CrowdfundingProject/')
api.add_resource(Project,'/CrowdfundingProject/<string:project_id>')
