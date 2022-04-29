import time
import unittest
from selenium import webdriver
from Pages.MainPage import MainPageCLass
from Pages.LoginPage import LoginPageClass
from Pages.PasswordPage import PasswordPageClass
from Pages.UserHomePage import UserHomePageClass
from Pages.CartPage import CartPageClass

class AmazonSimpleTestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.loginButton = MainPageCLass(self.driver)
        self.loginFieldText = LoginPageClass(self.driver)
        self.loginContinueButton = LoginPageClass(self.driver)
        self.passwordFieldText = PasswordPageClass(self.driver)
        self.passwordSigninButton = PasswordPageClass(self.driver)
        self.userHomePageCart = UserHomePageClass(self.driver)
        self.cartPageEmptyCart = CartPageClass(self.driver)
        self.cartPageDeleteFirstItem = CartPageClass(self.driver)

    def test_simpleTC(self):
        self.driver.get("https://www.amazon.com")
        self.loginButton.press_on_login_button()
        time.sleep(3)
        self.loginFieldText.fill_login_email_info("simonyan.semyon@gmail.com")
        time.sleep(3)
        self.loginContinueButton.press_on_continue_button()
        time.sleep(3)
        self.passwordFieldText.fill_password_field("4578867SAS$")
        time.sleep(3)
        self.passwordSigninButton.press_on_signin_button()
        time.sleep(3)
        self.userHomePageCart.press_on_cart_button()
        time.sleep(3)
        self.cartPageDeleteFirstItem.delete_first_item()
        time.sleep(3)
        self.cartPageEmptyCart.delete_all_products()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()