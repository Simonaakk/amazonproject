from Locators.LocatorsFile import mainPageLoginButtonLocator
from Common.CustomFind.FindElement import CustomFindElement

class MainPageCLass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = CustomFindElement(self.driver)

    def press_on_login_button(self):
        loginButton = self.findElement.find(*mainPageLoginButtonLocator)
        loginButton.click()


