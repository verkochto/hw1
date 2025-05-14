from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Firefox()

try:
    # Переход на страницу входа
    browser.get("http://the-internet.herokuapp.com/login")

    # Ввод логина
    login_input = browser.find_element(By.ID, "username")
    login_input.send_keys("tomsmith")

    # Ввод пароля
    pass_input = browser.find_element(By.ID, "password")
    pass_input.send_keys("SuperSecretPassword!")

    # Нажатие кнопки входа
    submit_btn = browser.find_element(By.TAG_NAME, "button")
    submit_btn.click()

    sleep(7)

    alert_text = browser.find_element(By.ID, "flash").text
    print(alert_text.strip())

    sleep(7)

finally:
    browser.quit()
