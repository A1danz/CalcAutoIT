import re

from helper.operation.plus_operation_helper import PlusOperationHelper
from model import TwoNumbersOperation
from tests.base.base_test import BaseTest


class TestPlusOperation(BaseTest):

    def test_plus_operation(self):
        self.app.navigation.open_default_calculator()

        numbers = TwoNumbersOperation(2, 7)

        helper = PlusOperationHelper(self.app, numbers)

        helper.do_operation()

        result_elem = helper.window.child_window(auto_id="CalculatorResults", control_type="Text")
        result_text = result_elem.window_text()
        result_number = "".join(re.findall(r'\d', result_text))

        assert str(numbers.first + numbers.second) == result_number, f"Ожидалось: {numbers.first + numbers.second}, получено: {result_number}"