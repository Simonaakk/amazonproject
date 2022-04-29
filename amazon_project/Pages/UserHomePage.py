from Locators.LocatorsFile import *

class UserHomePageClass():
    def __init__(self, driver):
        self.driver = driver

    def press_on_cart_button(self):
        cartButton = self.driver.find_element(*userHomePageCartButtonLocator)
        cartButton.click()

