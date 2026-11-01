import requests
from utils.logger import logger


def test_obtener_usuario(base_url, headers):
    logger.info("Iniciando prueba GET de usuario")

    url = f"{base_url}/users/2"
    response = requests.get(url, headers=headers)

    logger.info(f"GET {url} - Status: {response.status_code}")

    assert response.status_code == 200
    logger.info("Status code validado")

    assert "application/json" in response.headers["Content-type"]
    logger.info("Content-Type validado")

    data = response.json()

    assert isinstance(data, dict)
    assert "data" in data
    assert isinstance(data["data"], dict)

    for campo in ["id", "email", "first_name", "last_name"]:
        assert campo in data["data"]

    logger.info("Estructura JSON validada")

    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"
    logger.info("Contenido del usuario validado")

    assert response.elapsed.total_seconds() < 2
    logger.info("Tiempo de respuesta validado")

    logger.info("Prueba GET finalizada correctamente")


def test_crear_usuario(base_url, headers):
    logger.info("Iniciando prueba POST de usuario")

    url = f"{base_url}/users/"

    usuario = {
        "email": "test@test.com",
        "first_name": "Juan",
        "last_name": "Díaz",
        "job": "Jefe"
    }

    response = requests.post(url, headers=headers, json=usuario)

    logger.info(f"POST {url} - Status: {response.status_code}")

    assert response.status_code == 201
    logger.info("Status code validado")

    assert "application/json" in response.headers["Content-Type"]
    logger.info("Content-Type validado")

    data = response.json()

    for campo in ["email", "first_name", "last_name", "id"]:
        assert campo in data

    logger.info("Estructura JSON validada")

    assert data["email"] == usuario["email"]
    assert data["first_name"] == usuario["first_name"]
    logger.info("Contenido del usuario validado")

    assert response.elapsed.total_seconds() < 2
    logger.info("Tiempo de respuesta validado")

    logger.info("Prueba POST finalizada correctamente")


def test_eliminar_usuario(base_url, headers):
    logger.info("Iniciando prueba DELETE de usuario")

    url = f"{base_url}/users/2"
    response = requests.delete(url, headers=headers)

    logger.info(f"DELETE {url} - Status: {response.status_code}")

    assert response.status_code == 204
    logger.info("Status code validado")

    assert "Content-Type" not in response.headers
    assert len(response.content) == 0
    logger.info("Respuesta sin contenido validada")

    assert response.elapsed.total_seconds() < 2
    logger.info("Tiempo de respuesta validado")

    logger.info("Prueba DELETE finalizada correctamente")