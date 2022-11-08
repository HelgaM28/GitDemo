from selenium.webdriver.common.by import By


# self.driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
# self.driver.find_element(By.CLASS_NAME, "accept").click()

class LoginPage:

    def __init__(self, driver):  # class Constructor
        self.driver = driver

    username = (By.XPATH, "//input[@type='text']")  # tuple
    password = (By.ID, "password1")
    rememberuserid = (By.XPATH, "//label[@for='rememberuserid']")
    accept = (By.CLASS_NAME, "accept")
    logout =

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)  # * convert into tuple

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_rememberuserid(self):
        return self.driver.find_element(*LoginPage.rememberuserid)

    def get_accept(self):
        return self.driver.find_element(*LoginPage.accept)

    def get_logout
