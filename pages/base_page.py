from core.browser_action import BrowserActions

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = BrowserActions(driver)

    def open(self, url):
        self.driver.get(url)

    def __getattr__(self, item):
        return getattr(self.driver, item)

