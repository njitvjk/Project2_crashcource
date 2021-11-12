"""Child Class: Multiplication"""

from operations.calculation_base import Calculation

class Multiplication(Calculation):
    """Class having method to perform multiplication"""

    def get_output(self):
        """ function to multiply two  values a and b """
        return self.value_a * self.value_b
