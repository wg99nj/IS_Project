# calculator/calculation.py
import pandas as pd # type: ignore
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
