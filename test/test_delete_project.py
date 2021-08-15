from model.project import Project
import random
from fixture.project import ProjectHelper


def check_empty_list(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name="Test_NAME_TO_DELETE"))


def test_delete_project(app):
    check_empty_list(app)
    old_project_list = app.project.get_project_list()
    project_del = random.choice(old_project_list)
    app.project.delete_project(project_del.id)
    new_project_list = app.project.get_project_list()
    old_project_list.remove(project_del)
    assert old_project_list == new_project_list
