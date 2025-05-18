from abc import ABC, abstractmethod

from helper.operation.base_opeartion_helper import BaseOperationHelper
from model import TwoNumbersOperation


class BaseTwoNumbersOperationHelper(BaseOperationHelper, ABC):

    def __init__(self, app, numbers: TwoNumbersOperation):
        super().__init__(app)

        self.numbers = numbers

    @abstractmethod
    def do_operation(self):
        pass