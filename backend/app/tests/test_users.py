from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# test register user
def test_register_user(test_app_with_db):
    response = client.post(
        "/auth/register",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json={"email": "superuser@domain.com", "password": "123"},
    )
    assert response.status_code == 201
    assert "id" in response.json()
    # assert response.json()["url"] == "https://foo.bar"


# test login good password
# test login bad password
