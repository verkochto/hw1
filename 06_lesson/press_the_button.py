from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() 

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")


    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

    wait = WebDriverWait(driver, 20)
    result_element = wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "bg-success"), "Data loaded with AJAX get request."
        )
    )

    text = driver.find_element(By.CLASS_NAME, "bg-success").text
    print(text)

finally:
    driver.quit()
