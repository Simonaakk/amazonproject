import unittest
from Pages.MainPageFunctionality.MainPage import MainPageCLass
from Pages.LoginAndSignOutFunctionality.LoginPage import LoginPageClass
from Pages.LoginAndSignOutFunctionality.PasswordPage import PasswordPageClass
from Common.SetUp.SetUp import SetUpClass
from Common.Variables.VariablesFile import VariablesClass
from Pages.AddToCartFunctionality.MainPageSearchItem import MainPageSearchItemClass
from Pages.AddToCartFunctionality.SeachedItemPage import SearchedItemClass
from Pages.AddToCartFunctionality.FirstItemPage import FirstItemClass

class AddItemToCartClass(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.loginVar = VariablesClass()
        self.passwordVar = VariablesClass()
        self.itemName = VariablesClass()
        self.genSetUp()

        self.loginButton = MainPageCLass(self.driver)
        self.loginFieldText = LoginPageClass(self.driver)
        self.loginContinueButton = LoginPageClass(self.driver)
        self.passwordFieldText = PasswordPageClass(self.driver)
        self.passwordSigninButton = PasswordPageClass(self.driver)

        self.searchField = MainPageSearchItemClass(self.driver)
        self.searchButton = MainPageSearchItemClass(self.driver)
        self.searchedItem = SearchedItemClass(self.driver)
        self.addCart = FirstItemClass(self.driver)

    def test_simpleTC(self):
        self.driver.get("https://www.amazon.com")
        self.loginButton.press_on_login_button()
        self.loginFieldText.fill_login_email_info(self.loginVar.get_login())
        self.loginContinueButton.press_on_continue_button()

        self.passwordFieldText.fill_password_field(self.passwordVar.get_password())
        self.passwordSigninButton.press_on_signin_button()

        self.searchField.fill_search_field(self.itemName.get_item_name())
        self.searchButton.press_search_button()
        self.searchedItem.press_on_first_item()
        self.addCart.press_add_cart_button()

    def tearDown(self):
        self.driver.close()