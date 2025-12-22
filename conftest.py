import pytest
from utils.config_reader import ConfigReader
from core.driver_factory import DriverFactory

@pytest.fixture(scope="session")
def load_config():
    return ConfigReader()

@pytest.fixture(scope="function")
def browser():
    driver = DriverFactory.get_driver()
    yield driver
    DriverFactory.quit_driver()