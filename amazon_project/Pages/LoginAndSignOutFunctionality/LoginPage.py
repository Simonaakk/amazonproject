import time
from Locators.LocatorsFile import loginPageEmailFieldLocator, loginPageContinueButton
from Common.CustomFind.FindElement import CustomFindElement

class LoginPageClass():
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
        time.sleep(3)



