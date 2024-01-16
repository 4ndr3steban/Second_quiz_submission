from fastapi.testclient import TestClient
from app import app
import pytest

# Cliente de pruebas para la API
client = TestClient(app)

# Test para validar el endpoint para guardar una query en un post
def test_create_queryandpost():
    response = client.post("/userqueries/savequeryandpost", json={"query": {
                                                                            "date": "2023-11-15",
                                                                            "georange": "us",
                                                                            "numtop": 12,
                                                                            "ascentop": "string",
                                                                            "id_pos": 0},
                                                                    "post": {
                                                                            "username": "andres",
                                                                            "name": "query",
                                                                            "descript": "test"}})
    assert response.status_code == 201


# Test para validar el endpoint para guardar un comentario en un post
def test_create_comment():
    response = client.post("/userqueries/savecomment/2", json={
                                                            "user": "andres",
                                                            "comment": "test comment",
                                                            "id_post": "string"})
    assert response.status_code == 201


# Test para validar el endpoint para mostrar los posts
def test_show_post():
    response = client.get("/userqueries/showposts")

    assert response.status_code == 200


# Test para validar el endpoint para mostrar los comentarios de un post
def test_show_comments():
    response = client.get("/userqueries/showcomments/2")

    assert response.status_code == 200


# Test para validar el endpoint para mostrar una query para volver a usar
def test_show_querytouse():
    response = client.get("/userqueries/getquerytouse/1")

    assert response.status_code == 200

# Test para validar el endpoint para validar una consulta a Bigquery
def test_show_BigQuery1():
    response = client.get("/bigquery/consult?date=2023-11-15&georange=us&numtop=25&id_post=0")

    assert response.status_code == 200

# Test para validar el endpoint para validar una consulta a Bigquery
def test_show_BigQuery2():
    response = client.get("/bigquery/consult?date=2023-11-15&georange=intr&country=Belgium&numtop=10&ascentop=rising_&id_post=0")

    assert response.status_code == 200