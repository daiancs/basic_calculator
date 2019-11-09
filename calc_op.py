"""Class with calculator operations"""


class Calculator:
    def __init__(self):
        self._mem_value = 0

    def add(self, value):
        if not self._mem_value:
            self._mem_value = value
        else:
            self._mem_value += value

    def sub(self, value):
        pass

    def mult(self, value):
        pass

    def div(self, value):
        pass
