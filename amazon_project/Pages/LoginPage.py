from Locators.LocatorsFile import *

class LoginPageClass():
    def __init__(self, driver):
        self.driver = driver

    def fill_login_email_info(self, text):
        loginField = self.driver.find_element(*loginPageEmailFieldLocator)
        loginField.clear()
        loginField.send_keys(text)

    def press_on_continue_button(self):
        continueButton = self.driver.find_element(*loginPageContinueButton)
        continueButton.click()



