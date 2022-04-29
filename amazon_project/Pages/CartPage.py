from Locators.LocatorsFile import *
import time

class CartPageClass():
    def __init__(self, driver):
        self.driver = driver

    def delete_all_products(self):

        cartCount = self.driver.find_element(*cartPageCountLocator)
        numberOfProductsInCart = int(cartCount.text)

        while numberOfProductsInCart > 0:

            deleteButton = self.driver.find_element(*cartPageDeleteButton)
            deleteButton.click()
            numberOfProductsInCart -= 1
            time.sleep(3)

    def delete_first_item(self):
        deleteFirstItem = self.driver.find_element(*cartPageDeleteButton)
        deleteFirstItem.click()

