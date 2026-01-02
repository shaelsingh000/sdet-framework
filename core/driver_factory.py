from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import get_logger
import os

class DriverFactory:
    _driver = None

    @classmethod
    def get_driver(cls, headless=True):
        if cls._driver is None:
            logger = get_logger()

            chrome_options = Options()
            if headless:
                chrome_options.add_argument("--headless=new")

            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")

            driver_path = ChromeDriverManager().install()

            service = Service(executable_path=driver_path)

            cls._driver = webdriver.Chrome(
                service=service,
                options=chrome_options
            )

            logger.info("Chrome driver initialized successfully")

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
