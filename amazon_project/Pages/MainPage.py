from Locators.LocatorsFile import *

class MainPageCLass():
    def __init__(self, driver):
        self.driver = driver

    def press_on_login_button(self):
        loginButton = self.driver.find_element(*mainPageLoginButtonLocator)
        loginButton.click()


