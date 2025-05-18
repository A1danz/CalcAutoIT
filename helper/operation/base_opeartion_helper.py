from abc import ABC, abstractmethod

from helper.base_helper import BaseHelper


class BaseOperationHelper(BaseHelper, ABC):

    @abstractmethod
    def do_operation(self):
        pass