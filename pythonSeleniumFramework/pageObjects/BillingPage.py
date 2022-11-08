from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class BillingPage:
    def __init__(self, driver):
        self.driver = driver

    billing = (By.XPATH, "(//a[@href='http://shopping.beeyor.com/checkout/'])[3]")
    input = (By.XPATH, "(//input[@name='billing_first_name'])")
    input2 = (By.XPATH, "(//input[@name='billing_last_name'])")
    input3 = (By.XPATH, "(//input[@name='billing_address_1'])")
    input4 = (By.XPATH, "(//input[@name='billing_city'])")
    input5 = (By.XPATH, "(//input[@name='billing_postcode'])")
    input6 = (By.XPATH, "(//input[@name='billing_phone'])")
    input7 = (By.XPATH, "(//input[@name='billing_email'])")
    frame1 = (By.XPATH, "//iframe[@title='Secure card number input frame']")
    card_number = (By.XPATH, "//input[@aria-label='Credit or debit card number']")
    frame2 = (By.XPATH, "//iframe[@title='Secure expiration date input frame']")
    expiration_date = (By.CSS_SELECTOR, "input[aria-label='Credit or debit card expiration date']")
    frame3 = (By.XPATH, "//iframe[@title='Secure CVC input frame']")
    security_code = (By.CSS_SELECTOR, "input[aria-label='Credit or debit card CVC/CVV']")
    place_order = (By.ID, "place_order")

    def get_billing(self):
        return self.driver.find_element(*BillingPage.billing)

    def get_input(self):
        return self.driver.find_element(*BillingPage.input)

    def get_input2(self):
        return self.driver.find_element(*BillingPage.input2)

    def get_input3(self):
        return self.driver.find_element(*BillingPage.input3)

    def get_input4(self):
        return self.driver.find_element(*BillingPage.input4)

    def get_input5(self):
        return self.driver.find_element(*BillingPage.input5)

    def get_input6(self):
        return self.driver.find_element(*BillingPage.input6)

    def get_input7(self):
        return self.driver.find_element(*BillingPage.input7)

    def get_frame1(self):
        self.driver.switch_to.frame(
            self.driver.find_element(By.XPATH, "//iframe[@title='Secure card number input frame']"))
        return

    def get_card_number(self):
        return self.driver.find_element(*BillingPage.card_number)

    def get_home_window(self):
        HomeWindow = self.driver.window_handles
        self.driver.switch_to.window(HomeWindow[0])

    def get_frame2(self):
        self.driver.switch_to.frame(
            self.driver.find_element(By.XPATH, "//iframe[@title='Secure expiration date input frame']"))
        return

    def get_expiration_date(self):
        return self.driver.find_element(*BillingPage.expiration_date)

    def get_frame3(self):
        self.driver.switch_to.frame(
            self.driver.find_element(By.XPATH, "//iframe[@title='Secure CVC input frame']"))

    def get_security_code(self):
        return self.driver.find_element(*BillingPage.security_code)

    def get_place_order(self):
        return self.driver.find_element(*BillingPage.place_order)

#     driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Secure card number input frame']"))
# driver.find_element(By.XPATH, "//input[@aria-label='Credit or debit card number']").send_keys("4242424242424242")
# sleep(1)
# driver.switch_to.window(HomeWindow[0])
# driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Secure expiration date input frame']"))
# driver.find_element(By.CSS_SELECTOR, "input[aria-label='Credit or debit card expiration date']").send_keys("0226")
# driver.switch_to.window(HomeWindow[0])
# sleep(1)
# driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Secure CVC input frame']"))
# driver.find_element(By.CSS_SELECTOR, "input[aria-label='Credit or debit card CVC/CVV']").send_keys("123")
# sleep(1)
# driver.switch_to.window(HomeWindow[0])
# driver.find_element(By.ID, "place_order").click()
