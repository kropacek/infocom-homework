from abc import ABC, abstractmethod


class TimeCalculationStrategy(ABC):
    """Абстрактная стратегия расчета времени."""
    @abstractmethod
    def calculate(self, hours, hourly_rate):
        pass

class RegularTimeStrategy(TimeCalculationStrategy):
    """Стратегия для расчета обычного времени."""
    def calculate(self, hours, hourly_rate):
        return hours * hourly_rate

class OvertimeStrategy(TimeCalculationStrategy):
    """Стратегия для расчета сверхурочного времени."""
    def calculate(self, hours, hourly_rate):
        return hourly_rate * hours * 2

class TimeCalculator:
    """Контекст для расчета времени."""
    def __init__(self, strategy: TimeCalculationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: TimeCalculationStrategy):
        self.strategy = strategy

    def calculate_time(self, hours, hourly_rate):
        return self.strategy.calculate(hours, hourly_rate)
