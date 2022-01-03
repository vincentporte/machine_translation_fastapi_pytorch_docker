import pytest
import asyncio

from starlette.testclient import TestClient
from tortoise.contrib.starlette import register_tortoise
from fastapi_users.password import get_password_hash

from app.main import app
from app.database.models import UserModel

from decouple import config
from typing import Generator

DATABASE_URL = config("DATABASE_URL")

atreides_password_hash = get_password_hash("atreides")


@pytest.fixture(scope="module")
def client():
    client = TestClient(app)
    yield client  # testing happens here


@pytest.fixture(scope="module")
def client_with_db():
    client = TestClient(app)
    register_tortoise(
        app,
        db_url="sqlite://:memory:",
        # db_url=DATABASE_URL,
        modules={"models": ["app.database.models"]},
        generate_schemas=True,
    )

    with TestClient(app) as client_with_db:

        # testing
        yield client_with_db


@pytest.fixture(scope="module")
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()


@pytest.fixture(scope="module")
def verified_user() -> UserModel:
    return UserModel(
        email="verified@domain.com",
        hashed_password=atreides_password_hash,
        is_active=True,
        is_verified=True,
    )


@pytest.fixture(scope="module")
def db_verified_user(verified_user, event_loop: asyncio.AbstractEventLoop) -> UserModel:

    event_loop.run_until_complete(verified_user.save())

    return verified_user
