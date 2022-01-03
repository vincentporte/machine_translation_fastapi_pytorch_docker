import pytest
from starlette.testclient import TestClient

# from tortoise.contrib.fastapi import register_tortoise
from app.database.config import TORTOISE_ORM
from app.database.register import register_tortoise

from decouple import config

from app.main import app

# Tortoise.init_models(["app.database.models"], "models")
DATABASE_URL = config("DATABASE_URL")


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here


@pytest.fixture(scope="module")
def test_app_with_db():
    # set up
    client = TestClient(app)
    # app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)

    with TestClient(app) as test_client:

        # testing
        yield test_client
