from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product(self, product_id):
        self.driver.find_element(By.ID, f"add-to-cart-{product_id}").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
