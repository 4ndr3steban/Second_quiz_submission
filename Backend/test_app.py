from fastapi.testclient import TestClient
from app import app
import pytest

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "john_doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    assert response.json() == {"username": "john_doe", "email": "john.doe@example.com"}

def test_get_user():
    response = client.get("/users/john_doe")
    assert response.status_code == 200
    assert response.json() == {"username": "john_doe", "email": "john.doe@example.com"}

def test_get_invalid_user():
    response = client.get("/users/nonexistent_user")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

# Agregar más pruebas según sea necesario
