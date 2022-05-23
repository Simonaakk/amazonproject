import time
from Locators.LocatorsFile import firstItemAddToCartButtonLocator
from Common.CustomFind.FindElement import CustomFindElement

class FirstItemClass():
    def __init__(self, driver):
        self.driver =driver
        self.findElement = CustomFindElement(self.driver)

    def press_add_cart_button(self):
        addCartButton = self.findElement.find(*firstItemAddToCartButtonLocator)
        addCartButton.click()
        time.sleep(2)

