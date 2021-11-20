"""Child Class: Division"""

from operations.calculation_base import Calculation


class Division(Calculation):
    """ Division of two values a and b inherited from Parent class"""

    def get_output(self):
        """Function also checks for zero division error"""
        # return self.value_a / self.value_b
        try:
            return self.value_a / self.value_b
        except ZeroDivisionError as ex_div:
            print('Invalid Denominator Input:', ex_div)
            raise ZeroDivisionError from ex_div
