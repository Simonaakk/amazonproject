from Locators.LocatorsFile import searchedFirstItemLocator
from Common.CustomFind.FindElement import CustomFindElement

class SearchedItemClass():
    def __init__(self, driver):
        self.driver =driver
        self.findElement = CustomFindElement(self.driver)

    def press_on_first_item(self):
        searchedItem = self.findElement.find(*searchedFirstItemLocator)
        searchedItem.click()

