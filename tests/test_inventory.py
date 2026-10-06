# buscar titulo "Swag Labs"
# verificar menu
# verificar filtro
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import iniciar_sesion

def test_inventory(driver):
    iniciar_sesion(driver)

    espera = WebDriverWait(driver, 10)

    assert driver.title == "Swag Labs"

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

    productos = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )
    assert productos, "No se encontraron productos"
    assert productos[0].is_displayed()

    primero = productos[0]
    nombre = primero.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text
    precio = primero.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    assert nombre
    assert precio.startswith("$")

    print(f"Primer producto: {nombre} - {precio}")

    assert driver.find_element(
        By.ID, "react-burger-menu-btn"
    ).is_displayed()

    assert driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    ).is_displayed()