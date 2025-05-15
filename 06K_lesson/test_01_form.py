import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("browser", ["chrome"])
def test_form_submission(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("Only Chrome is supported in this test.")

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Заполнение всех полей
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

  
        driver.find_element(By.CSS_SELECTOR, "button").click()

 
        zip_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.NAME, "zip-code"))
        )

        zip_color = zip_field.value_of_css_property("border")
        assert "rgb(255, 0, 0)" in zip_color or "red" in zip_color.lower(), 

        green_fields = [
            "first-name", "last-name", "address", "email", "phone",
            "city", "country", "job-position", "company"
        ]

        for name in green_fields:
            el = driver.find_element(By.NAME, name)
            border_color = el.value_of_css_property("border")
            assert "rgb(0, 128, 0)" in border_color or "green" in border_color.lower(), f"{name} 

    finally:
        driver.quit()
