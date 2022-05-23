import unittest
from Pages.MainPageFunctionality.MainPage import MainPageCLass
from Pages.LoginAndSignOutFunctionality.LoginPage import LoginPageClass
from Pages.LoginAndSignOutFunctionality.PasswordPage import PasswordPageClass
from Pages.MainPageFunctionality.UserHomePage import UserHomePageClass
from Pages.CartFunctionality.CartPage import CartPageClass
from Common.SetUp.SetUp import SetUpClass
from Common.Variables.VariablesFile import VariablesClass


class DeleteFirstItemClass(unittest.TestCase, SetUpClass):
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
        self.userHomePageCart = UserHomePageClass(self.driver)
        self.cartPageEmptyCart = CartPageClass(self.driver)
        
    def test_simpleTC(self):
        self.driver.get("https://www.amazon.com")
        self.loginButton.press_on_login_button()
        self.loginFieldText.fill_login_email_info(self.loginVar.get_login())
        self.loginContinueButton.press_on_continue_button()
        self.passwordFieldText.fill_password_field(self.passwordVar.get_password())
        self.passwordSigninButton.press_on_signin_button()
        self.userHomePageCart.press_on_cart_button()
        self.cartPageEmptyCart.delete_all_products()

    def tearDown(self):
        self.driver.close()