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

#Main Page Home Button
mainPageHomeButtonLocator = (By.ID, "nav-logo-sprites")

#Main Page Search Field
mainPageSearchFieldLocator = (By.ID, "twotabsearchtextbox")
mainPageSearchButtonLocator = (By.ID, "nav-search-submit-button")

#Searched Page
searchedFirstItemLocator = (By.XPATH, "//img[@class='s-image']")

#First Item Page
firstItemAddToCartButtonLocator = (By.ID, "add-to-cart-button")

#Login Page Wrong Login Error
wrongLoginErrorTextLocator = (By.CLASS_NAME, "a-list-item")

#SignOut
accountButtonLocator = (By.ID, "nav-link-accountList")
signOutButtonLocator = (By.ID, "nav-item-signout")
