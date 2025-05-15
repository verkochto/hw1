import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.calculator_page import CalculatorPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # можно отключить для отладки
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_calculator_addition(driver):
    page = CalculatorPage(driver)
    page.open()
    page.set_delay(45)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result("15")

    assert result == "15", f"Ожидали '15', но получили '{result}'"
