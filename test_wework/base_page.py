from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator, value=None):
        if value is None:
            return self.driver.find_element(*locator)
        else:
            return self.driver.find_element(locator, value)

    def click_by_js(self, by, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, locator)))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(by, locator))

    def get_tips(self):
        return "OK"

