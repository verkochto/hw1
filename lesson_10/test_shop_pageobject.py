import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lesson_10.login_page import LoginPage
from lesson_10.products_page import ProductsPage
from lesson_10.cart_page import CartPage
from lesson_10.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.title("Оформление заказа с несколькими товарами")
@allure.description("Проверка общей суммы при покупке 3-х товаров через PageObject")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total(driver):
    with allure.step("Авторизация под стандартным пользователем"):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавление трёх товаров в корзину"):
        products = ProductsPage(driver)
        products.add_product("sauce-labs-backpack")
        products.add_product("sauce-labs-bolt-t-shirt")
        products.add_product("sauce-labs-onesie")
        products.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart = CartPage(driver)
        cart.click_checkout()

    with allure.step("Заполнение формы покупателя и получение суммы"):
        checkout = CheckoutPage(driver)
        checkout.fill_info("Иван", "Петров", "123456")
        total = checkout.get_total()

    with allure.step("Проверка, что сумма включает $58.29"):
        assert "$58.29" in total
