from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        assert isinstance(driver, WebDriver)
        self.driver = driver

    def wait_for_element_displayed(self, *locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(*locator))
