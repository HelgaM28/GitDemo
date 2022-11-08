from selenium.webdriver.common.by import By


class ShoppingPage:
    def __init__(self, driver):
        self.driver = driver

    item1 = (By.XPATH, "//a[text()='Add to cart']")
    item2 = (By.XPATH, "(//a[text()='Add to cart'])[2]")
    cart_content = (By.CSS_SELECTOR, "a[class='cart-contents']")
    button = (By.CSS_SELECTOR, "a[class='button checkout wc-forward wp-element-button']")

    def get_item1(self):
        return self.driver.find_element(*ShoppingPage.item1)

    def get_item2(self):
        return self.driver.find_element(*ShoppingPage.item2)

    def get_cart_content(self):
        return self.driver.find_element(*ShoppingPage.cart_content)

    def get_button(self):
        return self.driver.find_element(*ShoppingPage.button)
