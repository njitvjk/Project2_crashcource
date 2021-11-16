"""Child Class: Subtraction"""
import pprint

from operations.calculation_base import Calculation

class Subtraction(Calculation):
    """ Subtraction of two values a and b inherited from Parent class"""

    def get_output(self):
        """function returns subtracted value"""
        difference_of_values = 0.0
        for value in self.values:
            difference_of_values = difference_of_values - value
            pprint.pprint(value)
        return difference_of_values
