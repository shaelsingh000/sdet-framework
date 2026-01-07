from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login")

    def __init__(self, browser):
        self.browser = browser

    def login(self, user, password):
        self.browser.type(self.USERNAME, user)
        self.browser.type(self.PASSWORD, password)
        self.browser.click(self.SUBMIT)