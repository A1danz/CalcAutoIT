from helper.operation.base_opeartion_helper import BaseOperationHelper
from model import get_str


class LogOperationHelper(BaseOperationHelper):

    def __init__(self, app, number):
        super().__init__(app)

        self.number = get_str(number)

    def do_operation(self):
        self.print_all_elements()

        self.window.child_window(title=str("Очистить"), control_type="Button").click()

        self.window.child_window(title=str(self.number), control_type="Button").click()
        self.window.child_window(title="Логарифм", control_type="Button").click()
        self.window.child_window(title="Равно", control_type="Button").click()

