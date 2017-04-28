from Pages.BasePage import *
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    GO_BUTTON = (By.ID, 'submit')

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        MainPage.wait_for_element_displayed(self, MainPage.GO_BUTTON)
        element = self.driver.find_element(*MainPage.GO_BUTTON)
        element.click()
