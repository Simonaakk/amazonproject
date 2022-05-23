from selenium import webdriver

class SetUpClass():
    def genSetUp(self):
        self.driver = webdriver.Chrome("..\\Common\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
