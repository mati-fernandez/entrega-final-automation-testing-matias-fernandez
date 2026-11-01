from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger


def test_inventory(driver):
    logger.info("Iniciando prueba del inventario")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    driver.get("https://www.saucedemo.com/")
    logger.info("Página de login abierta")

    login_page.login("standard_user", "secret_sauce")
    logger.info("Login realizado")

    productos = inventory_page.obtener_productos()

    assert len(productos) > 0
    logger.info(f"Cantidad de productos encontrados: {len(productos)}")

    assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
    logger.info("Nombre del primer producto validado")

    assert inventory_page.obtener_precio_primer_producto() == "$29.99"
    logger.info("Precio del primer producto validado")

    assert inventory_page.menu_visible()
    logger.info("Menú visible")

    assert inventory_page.filtro_visible()
    logger.info("Filtro visible")

    logger.info("Prueba del inventario finalizada correctamente")