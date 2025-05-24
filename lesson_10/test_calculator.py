import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lesson_10.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.title("Сложение чисел в калькуляторе")
@allure.description("Проверка правильности сложения 7 + 8 с задержкой отображения результата")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_addition(driver):
    page = CalculatorPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        page.open()

    with allure.step("Устанавливаем задержку отображения результата в 45 секунд"):
        page.set_delay(45)

    with allure.step("Вводим выражение: 7 + 8 ="):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Получаем результат и сравниваем с ожидаемым значением"):
        result = page.get_result("15")
        assert result == "15", f"Ожидали '15', но получили '{result}'"
