from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TradePage:
    def __init__(self, driver):
        self.driver = driver

    symbol = (By.CSS_SELECTOR, "input[id='navigation-symbol-search']")
    symbol_confirm = (By.CSS_SELECTOR, "input[id='navigation-symbol-search']")
    side = (By.XPATH, "//button[@data-testid='TradeButton-buy']")
    quantity = (By.XPATH, "//input[@type='number']")
    review = (By.CSS_SELECTOR, "#review-order-button")
    sender = (By.CSS_SELECTOR, "#send-order-button")
    notification = (By.XPATH, "//div[text()= 'Notifications']")
    original_message = (By.XPATH, "(//div[@class='NotificationCardstyled__Text-liTWMR fhanmg'])[1]")

    # self.driver.find_element(By.CSS_SELECTOR, "input[id='navigation-symbol-search']").send_keys("TW")
    # self.driver.find_element(By.XPATH, "//input[@type='number']").click()
    def get_symbol(self):
        return self.driver.find_element(*TradePage.symbol)

    def get_symbol_confirm(self):
        return self.driver.find_element(*TradePage.symbol_confirm)

    def get_side(self):
        return self.driver.find_element(*TradePage.side)

    def get_quantity(self):
        return self.driver.find_element(*TradePage.quantity)

    def get_quantity_input(self):
        return self.driver.find_element(*TradePage.quantity)

    def get_review(self):
        return self.driver.find_element(*TradePage.review)

    def get_sender(self):
        return self.driver.find_element(*TradePage.sender)

    def get_notification(self):
        return self.driver.find_element(*TradePage.notification)

    def get_order_confirmation(self):
        original_confirmation = []
        original_message = [
            self.driver.find_element(*TradePage.original_message).text]

        for records in original_message:
            original_confirmation.append(records)
        assert original_message == original_confirmation
        return original_message
