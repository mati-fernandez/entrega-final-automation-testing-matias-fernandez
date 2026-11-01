from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.reader import read_productos_json
from utils.logger import logger


def test_cart(driver):
    logger.info("Iniciando prueba del carrito")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    driver.get("https://www.saucedemo.com/")
    logger.info("Página de login abierta")

    login_page.login("standard_user", "secret_sauce")
    logger.info("Login realizado")

    producto = read_productos_json()[0]
    logger.info(f"Producto seleccionado: {producto['nombre']}")

    inventory_page.agregar_producto(producto["nombre"])
    logger.info("Producto agregado al carrito")

    assert inventory_page.obtener_contador_carrito() == "1"
    logger.info("Contador del carrito validado")

    inventory_page.ir_al_carrito()
    logger.info("Navegación al carrito realizada")

    assert cart_page.obtener_nombre_producto() == producto["nombre"]
    logger.info("Nombre del producto validado")

    assert cart_page.obtener_precio_producto() == producto["precio"]
    logger.info("Precio del producto validado")

    logger.info("Prueba del carrito finalizada correctamente")