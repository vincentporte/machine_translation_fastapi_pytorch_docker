from fastapi.testclient import TestClient

from app.main import app
from app.services.users import current_active_user
from app.database.models import UserModel

client = TestClient(app)


def test_ner(client_with_db: TestClient, verified_user: UserModel) -> None:
    # Authenticate the user
    app.dependency_overrides[current_active_user] = lambda: verified_user

    sentence = "500 flyers"

    response = client.post("/ner", json={"sentence": sentence})

    assert "ner" in response.json()
    assert response.json()["entities"] == [
        {"text": "500", "entity": "EXEMPLAIRES", "pos": 0, "start": 0, "end": 3},
        {"text": "flyers", "entity": "PRODUCT", "pos": 1, "start": 4, "end": 10},
    ]
    assert response.status_code == 200
