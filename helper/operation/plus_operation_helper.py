from helper.operation.base_two_numbers_operation_helper import BaseTwoNumbersOperationHelper


class PlusOperationHelper(BaseTwoNumbersOperationHelper):

    def do_operation(self):
        self.window.child_window(title=str("Очистить"), control_type="Button").click()

        self.window.child_window(title=str(self.numbers.first_str), control_type="Button").click()
        self.window.child_window(title="Плюс", control_type="Button").click()
        self.window.child_window(title=str(self.numbers.second_str), control_type="Button").click()
        self.window.child_window(title="Равно", control_type="Button").click()
