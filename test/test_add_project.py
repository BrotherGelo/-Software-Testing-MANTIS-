from model.project import Project


def test_add_new_project(app):
    project = Project(name="Test_NAME", description="TEST_Description", status="release")
    old_project_list = app.soap.get_projects_list(username=app.config['webadmin']['username'],
                                              password=app.config['webadmin']['password'])
    app.project.create_project(project)
    new_project_list = app.project.get_project_list()
    old_project_list.append(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)