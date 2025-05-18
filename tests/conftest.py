import pytest

from app import ApplicationManager


@pytest.fixture(scope="session")
def app_manager():
    app = ApplicationManager()
    yield app
    app.close()