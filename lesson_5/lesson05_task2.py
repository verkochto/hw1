from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    blue_button.click()

    sleep(45)  
finally:
    driver.quit()
