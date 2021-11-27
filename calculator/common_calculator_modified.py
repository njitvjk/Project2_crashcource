import math

from calculator.calculator_history1 import CalculatorHistory


class Common_calculator(CalculatorHistory):

    def add(self, a, b):
        result = sum(a, b)
        self.add_to_history(result)
        return result

    def add_three_values(self, a, b, c):
        result = a + b + c
        self.add_to_history(result)
        return result

    def cal_subtract(self, a, b):
        result = a - b
        self.add_to_history(result)
        return result

    def cal_multiplication(self, nums):
        result = math.prod(nums)
        self.add_to_history(result)
        return result

    def division(self, a, b):
        result = a / b
        self.add_to_history(result)
        return result

    def add_to_history(self, result):
        self.calculation_history.append(result)
