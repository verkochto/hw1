from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("http://uitestingplayground.com/dynamicid")

    blue_button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
    blue_button.click()
    blue_button.click()
    sleep(40)  
finally:
    driver.quit()
