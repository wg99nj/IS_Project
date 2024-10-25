# tests/test_command_loader.py
from calculator.command_loader import CommandLoader

def test_load_commands():
    commands = CommandLoader.load_commands()
    assert "add" in commands
    assert "mean" in commands