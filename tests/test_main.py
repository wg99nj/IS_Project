import pytest
from calculator.command_loader import CommandLoader

@pytest.mark.parametrize("command_name, args, expected", [
    ("add", (3, 2), 5),
    ("subtract", (5, 2), 3),
    ("divide", (10, 2), 5),
    ("mean", (2, 4, 6), 4),
    ("median", (1, 2, 3), 2),
])
def test_command_execution(command_name, args, expected):
    commands = CommandLoader.load_commands()
    command = commands[command_name]
    result = command.execute(*args)
    assert result == expected