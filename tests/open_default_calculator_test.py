import pytest

from tests.base.base_test import BaseTest


class TestOpenDefaultCalculator(BaseTest):

    def test_open_default_calculator(self):
        self.app.navigation.open_default_calculator()

        header_text = self.app.header_helper.get_header()

        assert header_text == "Обычный", f"Ожидалось 'Обычный', но получено '{header_text}'"

