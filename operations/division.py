"""Child Class: Division"""

from operations.calculation_base import Calculation

class Division(Calculation):
    """ Division of two values a and b inherited from Parent class"""

    def get_output(self):
        """Function also checks for zero division error"""
        #return self.value_a / self.value_b
        print("====================division:==========================")
        result = self.values[0]
        for value in self.values:
            result = result / value
            print("result:", result)
            print("value:", value)
        return result
