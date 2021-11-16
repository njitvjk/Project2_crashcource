"""Child Class: Addition"""

from operations.calculation_base import Calculation

class Addition(Calculation):
    """ Addition of two values a and b inherited from Parent class"""

    def get_output(self):
        """function returns the addition result"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values
