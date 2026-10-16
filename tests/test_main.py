from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_application_info():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["application"] == "TechApp API"
    assert response.json()["message"] == "API funcionando"


def test_health_returns_healthy_status():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
