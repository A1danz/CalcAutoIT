class BaseHelper:
    def __init__(self, app_manager):
        self.app = app_manager.app
        self.window = app_manager.window

    def print_all_elements(self):
        self.window.print_control_identifiers()

