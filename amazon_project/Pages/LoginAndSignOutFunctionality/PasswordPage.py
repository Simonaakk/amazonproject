import time
from Locators.LocatorsFile import passwordPagePassworFieldLocator, pssswordPageSigninButton

class PasswordPageClass():
    def __init__(self, driver):
        self.driver = driver

    def fill_password_field(self, text):
        passwordField = self.driver.find_element(*passwordPagePassworFieldLocator)
        passwordField.clear()
        passwordField.send_keys(text)
        time.sleep(3)

    def press_on_signin_button(self):
        passwordSigninButton = self.driver.find_element(*pssswordPageSigninButton)
        passwordSigninButton.click()
        time.sleep(3)