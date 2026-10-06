import pytest
import logging
from pathlib import Path
from selenium import webdriver


SCREENSHOTS_DIR = Path("reports/screenshots")

LOGS_DIR = Path("reports/logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOGS_DIR / "test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@pytest.fixture
def driver():
    navegador = webdriver.Chrome()
    yield navegador
    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")

        if driver:
            SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

            nombre = f"{item.name}.png"
            ruta = SCREENSHOTS_DIR / nombre

            driver.save_screenshot(str(ruta))