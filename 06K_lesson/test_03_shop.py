import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"
EXPECTED_TOTAL = "$58.29"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Запуск без GUI
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_shop_total_price(driver):
    driver.get(BASE_URL)

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Проверка успешного входа
    assert "inventory.html" in driver.current_url, (
        f"Ошибка авторизации. Ожидался переход на 'inventory.html', "
        f"но текущий URL: {driver.current_url}"
    )

    # Добавление товаров в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переход к оформлению заказа
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # Проверка суммы заказа
    total_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_label.text

    assert EXPECTED_TOTAL in total_text, (
        f"Ожидалась сумма {EXPECTED_TOTAL}, но получено: {total_text}"
    )
