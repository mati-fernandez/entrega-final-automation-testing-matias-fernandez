from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import iniciar_sesion


def test_login_exitoso(driver):
    iniciar_sesion(driver)

    assert driver.current_url.endswith("/inventory.html")

    espera = WebDriverWait(driver, 10)

     # Validacion texto
    logo = espera.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "app_logo")
        )
    )
    
    assert logo.text == "Swag Labs"

    titulo = espera.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='title']")
        )
    )
    assert titulo.text == "Products"

    




