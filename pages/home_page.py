from pages.base_page import BasePage

class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.open(url)