import pytest
from utils.config_reader import ConfigReader

@pytest.fixture(scope="session")
def load_config():
    return ConfigReader