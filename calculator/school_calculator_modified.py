import math

from calculator.calculator_history import CalculatorHistory
from calculator.common_calculator_modified import Common_calculator
from operations.school_operations import ITrigonometryCalci


class SchoolCalculator(Common_calculator, ITrigonometryCalci,CalculatorHistory):

    def sin_of(self, x):
        result= math.sin(x)
        self.add_to_history(result)
        return result

    def cos_of(self, x):
        result = math.cos(x)
        self.add_to_history(result)
        return result

    def tan_of(self, x):
        result= math.tan(x)
        self.add_to_history(result)
        return result

    def add_to_history(self,result):
        self.calculation_history.append(result)