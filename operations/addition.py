"""Child Class: Addition"""

from operations.calculation_base import Calculation

class Addition(Calculation):
    """ Addition of two values a and b inherited from Parent class"""

    def get_output(self):
        """function returns the addition result"""
        return self.value_a + self.value_b
