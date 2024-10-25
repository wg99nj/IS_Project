from plugins.basic_plugins import AddCommand, SubtractCommand, DivideCommand
from plugins.statistics_plugins import MeanCommand, MedianCommand

class CommandLoader:
    @staticmethod
    def load_commands():
        return {
            "add": AddCommand(),
            "subtract": SubtractCommand(),
            "divide": DivideCommand(),
            "mean": MeanCommand(),
            "median": MedianCommand(),
        }
