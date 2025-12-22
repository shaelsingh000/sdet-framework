import pytest
from utils.logger import get_logger
from utils.config_reader import ConfigReader

@pytest.mark.usefixtures("load_config")
class BaseTest:
    logger = get_logger()

    