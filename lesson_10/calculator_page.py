from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class CalculatorPage:
    """
    PageObject для страницы калькулятора.
    Предоставляет методы для взаимодействия с UI: установка задержки, ввод значений и получение результата.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса CalculatorPage.

        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self) -> None:
        """
        Открывает калькулятор
        """
        self.driver.get(self.url)

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку (delay) перед отображением результата
        """
        delay_input: WebElement = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, value: str) -> None:
        """
        Нажимает на кнопку с заданным значением на калькуляторе
        """
        button: WebElement = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    def get_result(self, expected_text: str, timeout: int = 50) -> str:
        """
        Ожидает появления заданного текста на экране калькулятора и возвращает его.

       
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_text)
        )
        return self.driver.find_element(By.CLASS_NAME, "screen").text
