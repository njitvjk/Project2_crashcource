"""Child Class: Multiplication"""

from operations.calculation_base import Calculation

class Multiplication(Calculation):
    """Class having method to perform multiplication"""

    def get_output(self):
        """ function to multiply two  values a and b """
        result = 1.0
        for value in self.values:
            result = result * value
        return result
