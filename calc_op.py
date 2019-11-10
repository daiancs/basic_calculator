"""Class with calculator operations"""


class Calculator:

    def __init__(self):
        self._mem_value = 0
        self._operation = None
        self.operations_dict = {
            "add": self.add,
            "sub": self.sub,
            "mult": self.mult,
            "div": self.div
        }

    @property
    def memvalue(self):
        return self._mem_value

    def clear(self):
        self._mem_value = 0
        self._operation = None

    def operation(self, value, operator):
        try:
            value = float(value)
        except Exception:
            value = 0

        if not self._operation:
            if operator != "eq":
                self._operation = operator
                self._mem_value = value
        else:
            self._mem_value = self.operations_dict[self._operation](self._mem_value, value)

            if operator == "eq":
                self._operation = None
            else:
                self._operation = operator
            return True

        # print(f"Mem={self._mem_value}, Op={self._operation}")
        return False

    @staticmethod
    def add(value1, value2):
        return value1 + value2

    @staticmethod
    def sub(value1, value2):
        return value1 - value2

    @staticmethod
    def mult(value1, value2):
        return value1 * value2

    @staticmethod
    def div(value1, value2):
        return value1 / value2
