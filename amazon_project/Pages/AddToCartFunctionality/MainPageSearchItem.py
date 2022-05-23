from Locators.LocatorsFile import mainPageHomeButtonLocator, mainPageSearchFieldLocator, mainPageSearchButtonLocator
from Common.CustomFind.FindElement import CustomFindElement

class MainPageSearchItemClass():
    def __init__(self, driver):
        self.driver =driver
        self.findElement = CustomFindElement(self.driver)

    def press_home_button(self):
        homeButton = self.findElement.find(*mainPageHomeButtonLocator)
        homeButton.click()

    def fill_search_field(self, itemName):
        searchField = self.findElement.find(*mainPageSearchFieldLocator)
        searchField.clear()
        searchField.send_keys(itemName)

    def press_search_button(self):
        searchButton = self.findElement.find(*mainPageSearchButtonLocator)
        searchButton.click()

