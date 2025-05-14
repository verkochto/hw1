from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--start-maximized")


service = Service()

# Инициализация браузера
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://uitestingplayground.com/classattr")

    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
    )))

    button.click()

    alert = wait.until(EC.alert_is_present())
    alert.accept()

    time.sleep(1)  

finally:
    driver.quit()
