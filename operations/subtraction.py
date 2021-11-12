"""Child Class: Subtraction"""

from operations.calculation_base import Calculation

class Subtraction(Calculation):
    """ Subtraction of two values a and b inherited from Parent class"""

    def get_output(self):
        """function returns subtracted value"""
        return self.value_a - self.value_b
