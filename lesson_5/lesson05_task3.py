from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Запускаем Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")

    # "Sky"
    input_field.send_keys("Sky")
    sleep(5)  

    input_field.clear()
    sleep(5)

    input_field.send_keys("Pro")
    sleep(5)

finally:
    # Закрываем браузер
    driver.quit()
