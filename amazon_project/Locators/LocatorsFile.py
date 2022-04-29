from selenium.webdriver.common.by import By

#Main Page

mainPageLoginButtonLocator = (By.XPATH, "//a[@data-csa-c-content-id='nav_ya_signin']")

#Login Page

loginPageEmailFieldLocator = (By.XPATH, "//input[@name='email']")
loginPageContinueButton = (By.XPATH, "//input[@id='continue']")

#Password Page

passwordPagePassworFieldLocator = (By.ID, "ap_password")
pssswordPageSigninButton = (By.ID, "signInSubmit")

#User Home Page

userHomePageCartButtonLocator = (By.ID, "nav-cart")

#Cart Page

cartPageCountLocator = (By.ID, "nav-cart-count")
cartPageDeleteButton = (By.XPATH, "(//input[@value='Delete'])[1]")
