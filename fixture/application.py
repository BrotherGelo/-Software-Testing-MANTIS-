from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
#driver = webdriver.Firefox(options=options, executable_path="C:\Windows\SysWOW64\geckodriver.exe")

class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(options=options, executable_path="C:\Windows\SysWOW64\geckodriver.exe")
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("My View").click()

    def destroy(self):
        self.wd.quit()
