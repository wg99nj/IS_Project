# plugins/basic_plugins.py
class AddCommand:
    def execute(self, a: float, b: float) -> float:
        return a + b

class SubtractCommand:
    def execute(self, a: float, b: float) -> float:
        return a - b

class DivideCommand:
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b