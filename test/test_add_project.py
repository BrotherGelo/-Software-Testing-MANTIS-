from model.project import Project


def test_add_new_project(app):
    project = Project(name="Test_NAME", description="TEST_Description", status="release")
    app.project.create_project(project)