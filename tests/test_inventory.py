from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger


def test_inventory(driver):
    try:
        logger.info("Iniciando prueba del inventario")

        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        logger.info("Ingresando a la página web...")
        driver.get("https://www.saucedemo.com/")
        logger.info("Página de login abierta")

        logger.info("Ingresando credenciales válidas para iniciar sesión...")
        login_page.login("standard_user", "secret_sauce")
        logger.info("Login realizado")

        logger.info("Obteniendo productos...")
        productos = inventory_page.obtener_productos()
        logger.info("Productos de la página web capturados")

        logger.info("Calculando cantidad de productos...")
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
    except Exception:
        logger.exception("Error durante la prueba de inventario")
        raise