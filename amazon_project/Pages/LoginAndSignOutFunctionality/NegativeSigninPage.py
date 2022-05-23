import time
from Locators.LocatorsFile import loginPageEmailFieldLocator, loginPageContinueButton, wrongLoginErrorTextLocator
from Common.CustomFind.FindElement import CustomFindElement

class NegativeLoginPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = CustomFindElement(self.driver)

    def fill_login_email_info(self, text):
        loginField = self.findElement.find(*loginPageEmailFieldLocator)
        loginField.clear()
        loginField.send_keys(text)
        time.sleep(3)

    def press_on_continue_button(self):
        continueButton = self.findElement.find(*loginPageContinueButton)
        continueButton.click()