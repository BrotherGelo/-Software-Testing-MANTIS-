from model.project import Project
import random
import string
from fixture.project import ProjectHelper


def test_delete_project(app):
    check_empty_list(app)
    old_project_list = app.soap.get_project_list()
    project_del = random.choice(old_project_list)
    app.project.delete_project(project_del)
    new_project_list = app.soap.get_project_list()
    old_project_list.remove(project_del)
    assert old_project_list == new_project_list


def check_empty_list(app):
    if len(app.soap.get_project_list()) == 0:
        app.project.create_project(Project(name="Test_NAME_TO_DELETE"))


def random_name(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])