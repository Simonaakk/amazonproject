from selenium.webdriver.common.action_chains import ActionChains
from Locators.LocatorsFile import accountButtonLocator, signOutButtonLocator
from Common.CustomFind.FindElement import CustomFindElement

class SignOutClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = CustomFindElement(self.driver)

    def sign_out(self, driver):
        hoverMouse = ActionChains(driver)
        accountButton = self.findElement.find(*accountButtonLocator)
        hoverMouse.move_to_element(accountButton).perform()
        signOutButton = self.findElement.find(*signOutButtonLocator)
        hoverMouse.move_to_element(signOutButton).click().perform()