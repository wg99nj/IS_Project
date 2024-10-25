import pandas as pd 

class Calculation:
    history = pd.DataFrame(columns=["operation", "input", "result"])

    @classmethod
    def add_to_history(cls, operation: str, input_values: tuple, result: float):
        cls.history = cls.history.append({
            "operation": operation,
            "input": input_values,
            "result": result
        }, ignore_index=True)

    @classmethod
    def get_last_calculation(cls):
        return cls.history.iloc[-1] if not cls.history.empty else None

    @classmethod
    def get_history(cls):
        return cls.history
