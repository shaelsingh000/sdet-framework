from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.browser_action import BrowserActions

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.driver = BrowserActions(driver)
        