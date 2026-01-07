from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BrowserActions:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def upload_file(self, locator, file_path):
        self.driver.find_element(*locator).send_keys(file_path)

    def select_by_text(self, locator, text):
        Select(self.driver.find_element(*locator)).select_by_visible_text(text)
