from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )

    # находим теги <img> после загрузки
    images = driver.find_elements(By.TAG_NAME, "img")

    # Проверим, что хотя бы 3 картинки есть
    if len(images) >= 3:
        src_value = images[2].get_attribute("src")  # Индексация с нуля — это 3-я картинка
        print(src_value)
    else:
        print("Картинок меньше 3-х!")

finally:
    driver.quit()
