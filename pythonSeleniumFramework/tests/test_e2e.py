from time import sleep

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.TradePage import TradePage
from testLoginData.TestLoginData import TestData
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestE2E(BaseClass):
    def test_end_to_end(self, data_load):
        login = LoginPage(self.driver)
        login.get_username().send_keys(data_load["username"])
        login.get_password().send_keys(data_load["password"])
        login.get_rememberuserid().click()
        login.get_accept().click()
        trade = TradePage(self.driver)
        trade.get_symbol().send_keys("TW")
        trade.get_symbol_confirm().submit()
        trade.get_side().click()
        trade.get_quantity().click()
        for i in range(3):
            trade.get_quantity_input().send_keys(Keys.BACK_SPACE)
        trade.get_quantity_input().send_keys(15)
        trade.get_review().click()
        trade.get_sender().click()
        trade.get_notification().click()
        trade.get_order_confirmation()
        print("Rayhona changes 1")
        print("Rayhona changes 2")
        print("Davlagbek's changes1")
        print("Davlagbek's changes2")
        print("Davlagbek's changes3")


    @pytest.fixture(params=TestData.test_data)
    def data_load(self, request):
        return request.param

        #
        # self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("HelgaM28")
        # self.driver.find_element(By.ID, "password1").send_keys("Verberg28")
        # self.driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
        # self.driver.find_element(By.CLASS_NAME, "accept").click()
        # self.driver.find_element(By.CSS_SELECTOR, "input[id='navigation-symbol-search']").send_keys("TW")
        # self.driver.find_element(By.CSS_SELECTOR, "input[id='navigation-symbol-search']").submit()
        # self.driver.find_element(By.XPATH, "//button[@data-testid='TradeButton-buy']").click()
        # self.driver.find_element(By.XPATH, "//input[@type='number']").click()
        # for i in range(3):
        #     self.driver.find_element(By.XPATH, "//input[@type ='number']").send_keys(Keys.BACK_SPACE)
        # self.driver.find_element(By.XPATH, "//input[@type ='number']").send_keys(15)
        # sleep(1)
        # self.driver.find_element(By.CSS_SELECTOR, "#review-order-button").click()
        # self.driver.find_element(By.CSS_SELECTOR, "#send-order-button").click()
        # self.driver.find_element(By.XPATH, "//div[text()= 'Notifications']").click()
