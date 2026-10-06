import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def iniciar_sesion(driver):

    logging.info("Iniciando sesión en SauceDemo")

    driver.get("https://www.saucedemo.com/")

    espera = WebDriverWait(driver, 10)

    usuario = espera.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    password = driver.find_element(By.ID, "password")
    boton = driver.find_element(By.ID, "login-button")

    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")
    boton.click()

    espera.until(EC.url_contains("/inventory.html"))

    logging.info("Inicio de sesión exitoso")

    