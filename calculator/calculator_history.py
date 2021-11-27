from abc import abstractmethod


class CalculatorHistory:
    calculation_history = []

    def display_history(self):
        return self.calculation_history[-1]

    @abstractmethod
    def add_to_history(self, result):
        pass

