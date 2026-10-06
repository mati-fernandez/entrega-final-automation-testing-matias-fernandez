from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import iniciar_sesion

def test_carrito(driver):
    iniciar_sesion(driver)

    espera = WebDriverWait(driver, 10)

    producto = espera.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    nombre = producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    producto.find_element(By.TAG_NAME, "button").click()

    contador = espera.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )
    assert contador.text == "1"

    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    producto_carrito = espera.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )
    assert producto_carrito.text == nombre