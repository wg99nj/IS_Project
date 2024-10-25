import pytest
from calculator.calculation import Calculation

def test_add_to_history():
    Calculation.add_to_history("add", (1, 2), 3)
    last = Calculation.get_last_calculation()
    assert last["operation"] == "add"
    assert last["result"] == 3

def test_get_history():
    Calculation.add_to_history("subtract", (5, 3), 2)
    history = Calculation.get_history()
    assert len(history) > 0