from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        username = self.app.config['webadmin']['username']
        password = self.app.config['webadmin']['password']
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        project_list = []
        try:
            list_request = client.service.mc_projects_get_user_accessible(username, password)
            for i in list_request:
                project_list.append(i.name)
            return project_list
        except WebFault:
            return False