import math


# This is the Class taken as example for SOLID
class Calculator:

    def __init(self):
        self.calculation_history = []

    def cal_add(self, *nums):
        result = sum(nums)
        # self.add_to_history(result)
        return result

    def cal_substract(self, a, b):
        result = a - b
        # self.add_to_history(result)
        return result

    def cal_multplicaton(self, nums):
        result = math.prod(nums)
        self.add_to_history(result)
        return result

    def cal_division(self, a, b):
        result = a / b
        self.add_to_history(result)
        return result

    def cal_sin_of(self, x):
        result = math.sin(x)
        self.add_to_history(result)
        return result

    def cal_cos_of(self, x):
        result = math.cos(x)
        self.add_to_history(result)
        return result

    def cal_tan_of(self, x):
        result = math.tan(x)
        self.add_to_history(result)
        return result

    def display_history(self):
        return self.calculation_history[-1]

    def add_to_history(self, result):
        self.calculation_history.append(result)
