import re

from helper.operation.log_opertaion_helper import LogOperationHelper
from tests.base.base_test import BaseTest


class TestLogOperation(BaseTest):

    def test_log_operation(self):
        self.app.navigation.open_engineering_calculator()

        number = 1
        expected_result = 0

        helper = LogOperationHelper(self.app, number)
        helper.do_operation()

        result_elem = helper.window.child_window(auto_id="CalculatorResults", control_type="Text")
        result_text = result_elem.window_text()
        result_number = "".join(re.findall(r'\d', result_text))

        assert str(expected_result) == result_number, f"Ожидалось: {expected_result}, получено: {result_number}"



