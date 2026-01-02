from core.base_test import BaseTest
from pages.home_page import HomePage

class TestHomePage(BaseTest):
    def test_homepage_loads(self,browser,load_config):
        page = HomePage(browser)
        page.open(load_config.get("base_url"))
        assert browser.title is not None
