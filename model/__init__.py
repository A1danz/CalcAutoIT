from dataclasses import dataclass, field

DIGIT_MAP = {
    0: 'Ноль',
    1: 'Один',
    2: 'Два',
    3: 'Три',
    4: 'Четыре',
    5: 'Пять',
    6: 'Шесть',
    7: 'Семь',
    8: 'Восемь',
    9: 'Девять'
}


def get_str(number: int) -> str:
    return DIGIT_MAP[number]


@dataclass
class TwoNumbersOperation:
    first: int
    second: int

    first_str: str = field(init=False)
    second_str: str = field(init=False)

    def __post_init__(self):
        self.first_str = get_str(self.first)
        self.second_str = get_str(self.second)
