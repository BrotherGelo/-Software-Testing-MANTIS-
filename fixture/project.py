from model.project import Project
from selenium.webdriver.support.ui import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("My View").click()

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_projects_page()
        self.project_cache = None

    def delete_project(self, name):
        wd = self.app.wd
        self.open_projects_page()
        self.open_project(name)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)
        self.change_select_value("status", project.status)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.app.return_to_home_page()
            self.open_projects_page()
            self.project_cache = []
            for element in wd.find_elements_by_xpath("//tr[contains(@class, 'row-')]"
                                                     "[not(contains(@class, 'category'))][not(ancestor::a)]"):
                fields = element.find_elements_by_tag_name("td")
                id = fields[0].find_element_by_tag_name("a").get_attribute("href").split("=", 1)[1]
                name = fields[0].find_element_by_tag_name("a").text
                self.project_cache.append(Project(name=name, id=id))
        return list(self.project_cache)

    def open_project(self, project_name):
        wd = self.app.wd
        for element in wd.find_elements_by_xpath("//tr[contains(@class, 'row-')]"
                                                 "[not(contains(@class, 'category'))][not(ancestor::a)]"):
            fields = element.find_elements_by_tag_name("td")
            id = fields[0].find_element_by_tag_name("a").get_attribute("href").split("=", 1)[1]
            name = fields[0].find_element_by_tag_name("a").text
            if name == project_name:
                wd.find_element_by_link_text(name).click()
                break
