from helper.base_helper import BaseHelper


class NavigationHelper(BaseHelper):
    def open_default_calculator(self):
        self.__open_pane_menu("Обычный Калькулятор")

    def open_engineering_calculator(self):
        self.__open_pane_menu("Инженерный Калькулятор")

    def __open_pane_menu(self, item_title: str):
        print(self.window)
        nav_btn = self.window.child_window(auto_id="TogglePaneButton", control_type="Button")
        nav_btn.click_input()

        standard_btn = self.window.child_window(title=item_title, control_type="ListItem")
        standard_btn.wait('visible', timeout=5)

        standard_btn.click_input()
        standard_btn.wait_not('visible', timeout=5)


