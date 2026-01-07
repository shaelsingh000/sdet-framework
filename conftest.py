import pytest
import allure
from utils.config_reader import ConfigReader
from core.driver_factory import DriverFactory
from core.browser_action import BrowserActions

@pytest.fixture(scope="session")
def load_config():
    return ConfigReader()

@pytest.fixture(scope="function")
def browser():
    driver = DriverFactory.get_driver()
    actions = BrowserActions(driver)
    yield driver
    DriverFactory.quit_driver()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver",None)
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name = "Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )