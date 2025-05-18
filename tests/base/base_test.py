import pytest

from app import ApplicationManager


class BaseTest:
    def setup_method(self, method):
        pass

    @pytest.fixture(autouse=True)
    def setup_app(self, app_manager):
        self.app = app_manager