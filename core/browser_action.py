from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

class BrowserActions:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            timeout,
            poll_frequency=0.5,
            ignored_exceptions=[StaleElementReferenceException]
        )

    # ---------- WAITERS ----------

    def wait_for_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element not visible: {locator}")

    def wait_for_clickable(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"Element not clickable: {locator}")

    # ---------- ACTIONS ----------

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def click_js(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text, clear=True):
        element = self.wait_for_visible(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def scroll_into_view(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

    def upload_file(self, locator, file_path):
        element = self.wait_for_visible(locator)
        element.send_keys(file_path)

    def select_by_text(self, locator, text):
        element = self.wait_for_visible(locator)
        Select(element).select_by_visible_text(text)

    # ---------- ADVANCED ----------

    def hover(self, locator):
        element = self.wait_for_visible(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def get_text(self, locator):
        element = self.wait_for_visible(locator)
        return element.text
