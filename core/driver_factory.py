from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import get_logger

class DriverFactory:
    _driver = None
    @classmethod
    def get_driver(cls,headless=True):
        if cls._driver is None:
            logger = get_logger()
            options = Options()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--windown-size=1920,1080")

            service = Service(ChromeDriverManager().install)
            cls._driver = webdriver.Chrome(service=service,options=options)
            logger.info("Chrome Driver Intialized")
        return cls._driver
    
    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
            