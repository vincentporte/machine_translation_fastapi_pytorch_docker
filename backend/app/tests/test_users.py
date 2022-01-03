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


# test login good password
def test_register_user(test_app_with_db):
    response = client.post(
        "/auth/register",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json={"email": "superuser@domain.com", "password": "123"},
    )
    response = client.post(
        "/auth/login",
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={"username": "superuser@domain.com", "password": "123"},
    )
    print(response)
    print(response.json())
    assert response.status_code == 200
    assert "access_token" in response.json()


# test login bad password
def test_register_user(test_app_with_db):
    response = client.post(
        "/auth/register",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json={"email": "superuser@domain.com", "password": "123"},
    )
    response = client.post(
        "/auth/login",
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={"username": "superuser@domain.com", "password": "456"},
    )
    print(response)
    print(response.json())
    assert response.status_code == 400
    assert response.json()["detail"] == "LOGIN_BAD_CREDENTIALS"
