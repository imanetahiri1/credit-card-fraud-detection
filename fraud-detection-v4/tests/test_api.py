from fastapi.testclient import TestClient

from app.api import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_model_info() -> None:
    response = client.get("/model-info")

    assert response.status_code == 200
    assert response.json()["feature_count"] == 30


def test_prediction_rejects_missing_features() -> None:
    response = client.post(
        "/predict",
        json={"Time": 1.0, "Amount": 10.0},
    )

    assert response.status_code == 422