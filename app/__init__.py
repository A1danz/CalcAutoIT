from time import sleep

from pywinauto import Application

from config import APP_NAME
from helper.header_helper import HeaderHelper
from helper.navigation_helper import NavigationHelper


class ApplicationManager:
    def __init__(self):
        self.app = Application(backend="uia").start(APP_NAME)
        sleep(1)

        self.app = Application(backend="uia").connect(title_re="Калькулятор")
        self.window = self.app.window(title_re="Калькулятор")

        self.window.wait('visible', timeout=10)

        self.__init_helpers()

    def __init_helpers(self):
        self.navigation = NavigationHelper(self)
        self.header_helper = HeaderHelper(self)

    def close(self):
        self.app.kill()