from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class CouponPage:
    def __init__(self, driver):
        self.driver = driver

    coupon = (By.CSS_SELECTOR, "input[name='coupon_code']")
    apply_coupon = (By.XPATH, "//button[@name='apply_coupon']")
    alert = (By.XPATH, "//div[@role='alert']")

    def get_coupon(self):
        return self.driver.find_element(*CouponPage.coupon)

    def get_apply_coupon(self):
        return self.driver.find_element(*CouponPage.apply_coupon)

    def get_alert(self):
        return self.driver.find_element(*CouponPage.alert)