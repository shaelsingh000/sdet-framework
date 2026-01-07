from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login")

    def login(self, user, password):
        self.actions.send_keys(self.USERNAME, user)
        self.actions.send_keys(self.PASSWORD, password)
        self.actions.click(self.SUBMIT)
