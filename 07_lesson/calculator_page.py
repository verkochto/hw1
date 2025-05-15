from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, value):
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    def get_result(self, expected_text, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_text)
        )
        return self.driver.find_element(By.CLASS_NAME, "screen").text
