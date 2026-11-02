# Automatización QA - SauceDemo

Proyecto de automatización de pruebas funcionales y de API realizado con Python, Selenium y Pytest para el curso de Talento Tech.

## Tecnologías utilizadas

- Python
- Selenium
- Pytest
- pytest-html
- Requests
- python-dotenv
- Git
- GitHub

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

Configurar las variables de entorno creando un archivo `.env` en la raíz del proyecto:

```env
REQRES_API_KEY=tu_api_key
```

## Ejecución de las pruebas

Ejecutar toda la suite:

```bash
pytest
```

Pytest utiliza la configuración de `pytest.ini` para descubrir las pruebas dentro de `tests/` y generar automáticamente el reporte HTML.

También se puede ejecutar un módulo específico:

```bash
pytest tests/test_login.py
```

## Casos de prueba

### Login

- Acceder a SauceDemo.
- Probar credenciales válidas e inválidas.
- Verificar el acceso a `/inventory.html` cuando el login es exitoso.
- Validar el mensaje de error ante credenciales incorrectas.

### Catálogo

- Verificar el título de la página de inventario.
- Verificar que se muestre el logo `Swag Labs`.
- Verificar que se muestre el título `Products`.
- Comprobar que existan productos visibles.
- Obtener el nombre y precio del primer producto.
- Verificar elementos principales de la interfaz, como el menú y el filtro de productos.

### Carrito

- Agregar un producto al carrito.
- Verificar que el contador del carrito se actualice.
- Acceder al carrito.
- Validar el nombre y precio del producto agregado.

### API

- **GET:** obtener un usuario y validar el código de estado, headers, estructura y contenido JSON.
- **POST:** crear un usuario y validar la respuesta y los datos enviados.
- **DELETE:** eliminar un usuario y verificar el código de estado y la ausencia de contenido en la respuesta.

## Reportes y evidencias

- **Reporte HTML:** `reports/reporte.html`
- **Logs:** `reports/logs/test.log`
- **Capturas:** `reports/screenshots/`

Las capturas se generan automáticamente cuando falla una prueba y se adjuntan al reporte HTML.

El directorio `reports/` está excluido del control de versiones porque contiene archivos generados durante las ejecuciones.

El reporte HTML muestra cada prueba ejecutada, su estado y duración. Al abrir una prueba fallida, se puede consultar el detalle del error y la captura de pantalla adjunta, si corresponde.

