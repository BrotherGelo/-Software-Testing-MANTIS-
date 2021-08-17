import random
import string
from model.project import Project


def test_add_new_project(app):
    project_name = random_name("name", 7)
    project = (Project(name=project_name))
    old_project_list = app.soap.get_project_list()
    app.project.create_project(project)
    new_project_list = app.soap.get_project_list()
    old_project_list.append(project_name)
    assert sorted(old_project_list) == sorted(new_project_list)


def random_name(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])