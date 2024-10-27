# calculator/calculation.py

import pandas as pd
from typing import Any, Tuple

class Calculation:
    history = pd.DataFrame(columns=["operation", "input", "result"])

    @classmethod
    def add_to_history(cls, operation: str, inputs: Tuple[Any, ...], result: Any) -> None:
        new_entry = pd.DataFrame([{
            "operation": operation,
            "input": inputs,
            "result": result
        }])
        cls.history = pd.concat([cls.history, new_entry], ignore_index=True)

    @classmethod
    def get_history(cls) -> pd.DataFrame:
        return cls.history

    @classmethod
    def get_last_calculation(cls) -> pd.Series:
        """Retrieve the last calculation entry from the history."""
        if not cls.history.empty:
            return cls.history.iloc[-1]
        else:
            return pd.Series()  # Returns an empty Series if no history exists
