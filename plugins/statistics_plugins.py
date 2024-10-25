# plugins/statistics_plugins.py
from typing import List

class MeanCommand:
    def execute(self, *numbers: float) -> float:
        return sum(numbers) / len(numbers) if numbers else 0.0

class MedianCommand:
    def execute(self, *numbers: float) -> float:
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        if n == 0:
            return 0.0
        mid = n // 2
        if n % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0
        else:
            return sorted_numbers[mid]