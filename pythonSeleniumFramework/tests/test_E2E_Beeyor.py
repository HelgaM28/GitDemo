from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from pageObjects.CouponPage import CouponPage
from pageObjects.BillingPage import BillingPage
from pageObjects.ShoppingPage import ShoppingPage
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):
    def test_end_to_end(self):
        shopping = ShoppingPage(self.driver)
        shopping.get_item1().click()
        sleep(2)
        shopping.get_item2().click()
        shopping.get_cart_content().click()
        coupon = CouponPage(self.driver)
        coupon.get_coupon().send_keys("Tojtech Automation")
        coupon.get_apply_coupon().click()
        sleep(2)
        coupon.get_alert().click()
        billing = BillingPage(self.driver)
        billing.get_billing().click()
        billing.get_input().click()
        billing.get_input().send_keys("Volha")
        billing.get_input2().click()
        billing.get_input2().send_keys("Minovich")
        billing.get_input3().send_keys("1125 Banner av")
        billing.get_input4().send_keys("Brooklyn")
        billing.get_input5().send_keys("11235")
        billing.get_input6().send_keys("6467055603")
        billing.get_input7().send_keys("minowiczhelga@gmail.com")
        billing.get_frame1()
        billing.get_card_number().send_keys("4242424242424242")
        billing.get_home_window()
        billing.get_frame2()
        billing.get_expiration_date().send_keys("1234")
        billing.get_home_window()
        billing.get_frame3()
        billing.get_security_code().send_keys("981")
        billing.get_home_window()
        billing.get_place_order().click()