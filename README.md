# Automatización QA - SauceDemo

Proyecto de automatización de pruebas funcionales realizado con Python, Selenium y Pytest para el curso de Talento Tech.

## Tecnologías usadas

* Python
* Selenium
* Pytest
* pytest-html
* Git
* GitHub

## Instalación

Clonar el repositorio y acceder a la carpeta del proyecto.

Crear y activar un entorno virtual:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar las pruebas

Ejecutar toda la suite:

```bash
pytest
```

El reporte HTML se genera automáticamente en:

```text
reports/reporte.html
```
## Casos de prueba

### Login exitoso

* Acceder a SauceDemo.
* Ingresar credenciales válidas.
* Verificar el acceso a `/inventory.html`.
* Verificar que se muestre el logo `Swag Labs`.
* Verificar que se muestre `Products`.

### Catálogo

* Verificar el título de la página de inventario.
* Verificar que se muestre el logo `Swag Labs`.
* Verificar que se muestre el título `Products`.
* Verificar que existan productos visibles.
* Obtener el nombre y precio del primer producto.
* Verificar elementos principales de la interfaz, como el menú y el filtro de productos.

### Carrito

* Agregar el primer producto al carrito.
* Verificar que el contador del carrito se actualice.
* Acceder al carrito.
* Verificar que el producto agregado se encuentre presente.

## Reportes y evidencias

* Reporte HTML: `reports/reporte.html`
* Logs de ejecución: `reports/logs/test.log`
* Capturas de pantalla: `reports/screenshots/` (se generan automáticamente cuando un test falla)