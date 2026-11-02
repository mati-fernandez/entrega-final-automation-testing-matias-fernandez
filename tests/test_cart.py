from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.reader import read_productos_json
from utils.logger import logger


def test_cart(driver):
    try:
        logger.info("Iniciando prueba del carrito")

        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        logger.info("Ingresando a la página web de prueba...")
        driver.get("https://www.saucedemo.com/")
        logger.info("Página de login abierta")

        logger.info("Ingresando credenciales válidas para el inicio de sesión...")
        login_page.login("standard_user", "secret_sauce")
        logger.info("Login realizado")

        logger.info("Leyendo el primer producto del JSON")
        producto = read_productos_json()[0]
        logger.info(f"Producto seleccionado: {producto['nombre']}")

        logger.info("Agregando producto del JSON al carrito")
        inventory_page.agregar_producto(producto["nombre"])
        logger.info("Producto agregado al carrito")

        assert inventory_page.obtener_contador_carrito() == "1"
        logger.info("Contador del carrito validado")

        logger.info("Ir a la página del carrito...")
        inventory_page.ir_al_carrito()
        logger.info("Navegación al carrito realizada")

        assert cart_page.obtener_nombre_producto() == producto["nombre"]
        logger.info("Nombre del producto en carrito validado contra JSON")

        assert cart_page.obtener_precio_producto() == producto["precio"]
        logger.info("Precio del producto en carrito validado contra JSON")

        logger.info("Prueba del carrito finalizada correctamente")
    except Exception:
        logger.exception("Error durante la prueba del carrito")
        raise