from flask_restful import Resource
from models import CrowdfundingProject

class Projects(Resource):
    def get(self):
        try:
            projects = CrowdfundingProject.query.all()
            project_list = []
            for item in projects:
                i = {
                    'Id': item.Id,
                    'Building_id': item.Building_id,
                    'Address': item.Address,
                    'City': item.City,
                    'State': item.State
                }
                project_list.append(i)

            return { 'projects': project_list }



        except Exception as e:
            return {'error' : str(e)}



class Project(Resource):
    def get(self, project_id):
        try:

            project = CrowdfundingProject.query.get(project_id)
            i = {
                'Id': project.Id,
                'Building_id': project.Building_id,
                'Address': project.Address,
                'City': project.City,
                'State': project.State
            }

            return { 'project': i }



        except Exception as e:
            return { 'error': str(e) }

