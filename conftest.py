import pytest
import os
import base64
import pytest_html

from pathlib import Path
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return {"x-api-key": os.getenv("REQRES_API_KEY")}

SCREENSHOTS_DIR = Path("reports/screenshots")

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    navegador = webdriver.Chrome(options=options)
    yield navegador
    navegador.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")

        if driver:
            SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

            nombre = f"{item.name}.png"
            ruta = SCREENSHOTS_DIR / nombre

            driver.save_screenshot(str(ruta))

            imagen = base64.b64encode(ruta.read_bytes()).decode("utf-8")
            reporte.extras = [
                pytest_html.extras.png(imagen, name="Screenshot")
            ]
