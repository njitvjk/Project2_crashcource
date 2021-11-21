"""Child Class: Subtraction"""

from operations.calculation_base import Calculation
from operations.calculator_history import CalculationHistory


class Subtraction(Calculation,CalculationHistory):
    """ Subtraction of two values a and b inherited from Parent class"""
    def __init__(self, value_a, value_b):
        super().__init__(value_a, value_b)
        cal = Calculation(value_a, value_b)
        self.value_b = cal.get_value_b()
        self.value_a = cal.get_value_a()
        self.result=0

    def get_output(self):
        """function returns subtracted value"""
        self.result = self.value_a - self.value_b
        self.append_calculation_to_history()
        return self.result

    def append_calculation_to_history(self):  # implementing abstract method
        CalculationHistory.calculation_history.append(self.result)
