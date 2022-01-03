from fastapi.testclient import TestClient

from app.main import app
from app.core.users import current_active_user
from app.database.models import UserModel

client = TestClient(app)


def test_create_and_collect_products(
    client_with_db: TestClient, db_verified_user: UserModel
) -> None:

    # Authenticate the user
    app.dependency_overrides[current_active_user] = lambda: db_verified_user

    response = client_with_db.get("/products")
    print(response, response.text)

    source = "ff 21*297mm"
    translation = "format ferme 210 x 297 mm"

    response = client_with_db.post(
        "/products", json={"source": source, "translation": translation}
    )

    print(response)
    print(response.json())

    assert response.json()["source"] == source
    assert response.json()["translation"] == translation
    assert id in response.json()
    assert response.status_code == 200
