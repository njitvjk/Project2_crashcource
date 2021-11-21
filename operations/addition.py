"""Child Class: Addition"""

from operations.calculation_base import Calculation
from operations.calculator_history import CalculationHistory


class Addition(Calculation,CalculationHistory):
    """ Addition of two values a and b inherited from Parent class"""
    def __init__(self, value_a, value_b, value_c=0): # Method overloading
        super().__init__(value_a, value_b)
        cal = Calculation(value_a, value_b)
        self.value_b = cal.get_value_b()
        self.value_a = cal.get_value_a()
        self.result=0
        self.value_c=value_c

    def get_output(self):
        """function returns the addition result"""
        self.result=self.value_a + self.value_b+self.value_c
        self.append_calculation_to_history()
        print(self.result)
        return self.result

    def get_description(self):
        print("Performing Addition") # Method overriding

    def append_calculation_to_history(self): # implementing abstract method
        CalculationHistory.calculation_history.append(self.result)
        print(CalculationHistory.calculation_history)
