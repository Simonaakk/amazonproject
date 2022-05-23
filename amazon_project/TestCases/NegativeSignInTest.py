import time
import unittest
from Pages.MainPageFunctionality.MainPage import MainPageCLass
from Pages.LoginAndSignOutFunctionality.NegativeSigninPage import NegativeLoginPageClass
from Common.SetUp.SetUp import SetUpClass
from Common.Variables.VariablesFile import VariablesClass
from Pages.LoginAndSignOutFunctionality.PasswordPage import PasswordPageClass
from Common.CustomFind.FindElement import CustomFindElement
from Locators.LocatorsFile import wrongLoginErrorTextLocator

class AmazonSimpleTestClass(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.loginVar = VariablesClass()
        self.passwordVar = VariablesClass()
        self.itemName = VariablesClass()
        self.genSetUp()
        self.loginButton = MainPageCLass(self.driver)
        self.loginFieldText = NegativeLoginPageClass(self.driver)
        self.loginContinueButton = NegativeLoginPageClass(self.driver)
        self.wrongLogin = NegativeLoginPageClass(self.driver)
        self.passwordFieldText = PasswordPageClass(self.driver)
        self.passwordSigninButton = PasswordPageClass(self.driver)

    def test_simpleTC(self):
        self.driver.get("https://www.amazon.com")
        self.loginButton.press_on_login_button()
        self.loginFieldText.fill_login_email_info(self.loginVar.get_wrong_login())
        self.loginContinueButton.press_on_continue_button()
        try:
            self.passwordFieldText.fill_password_field(self.passwordVar)
        except:
            if self.wrongLogin.findElement.find(*wrongLoginErrorTextLocator):
                print("You entered a wrong e-mail address")
                exit(2)

    def tearDown(self):
        self.driver.close()