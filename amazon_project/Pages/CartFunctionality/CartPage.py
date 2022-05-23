import time
from Locators.LocatorsFile import cartPageCountLocator, cartPageDeleteButton
from Common.CustomFind.FindElement import CustomFindElement

class CartPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = CustomFindElement(self.driver)

    def delete_first_item(self):
        deleteFirstItem = self.findElement.find(*cartPageDeleteButton)
        deleteFirstItem.click()
        time.sleep(3)

    def delete_all_products(self):
        cartCount = self.findElement.find(*cartPageCountLocator)
        numberOfProductsInCart = int(cartCount.text)
        time.sleep(2)

        while numberOfProductsInCart > 0:
            #deleteButton = self.findElement.find(*cartPageDeleteButton)
            #deleteButton.click()
            self.delete_first_item()
            numberOfProductsInCart -= 1
            time.sleep(2)



