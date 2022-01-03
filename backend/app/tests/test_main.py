from starlette.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_status(test_app):
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "up"}


def test_home(test_app):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "msg": f"wercome on our character level sequence 2 sequence machine translation demo"
    }


# TESTS NON AUTHENT
# user whoami

# USERS CREATION
# register user 1
# register user 2
# login user 1

# TESTS AUTHENT
# user whoami
# create note user 1
# create note user 2
# get note user 1
# update note user 1
# update note user 2
# delete note user 1
# delete note user 2
# delete user 2
# delete user 1
