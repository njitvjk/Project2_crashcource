import math


from calculator.calculator_history import CalculatorHistory



class Common_calculator(CalculatorHistory):

    def add(self, a, b):
        result = sum(a, b)
        self.add_to_history(result)
        return result

    ##sOlid- principel 2
    def add_three_values(self, a, b, c):
        result = a + b + c
        self.add_to_history(result)
        return result

    def substract(self, a, b):
        result = a - b
        self.add_to_history(result)
        return result

    def cal_multplicaton(self, nums):
        result = math.prod(nums)
        self.add_to_history(result)
        return result

    def division(self, a, b):
        result = a / b
        self.add_to_history(result)
        return result

    def add_to_history(self,result):
        CalculatorHistory.calculation_history.append(result)

    #principle 3 accessing parent class
    def display_history(self):
        return super.display_history()
    #Principle 4
    def clear_calculator(self):
        CalculatorHistory.calculation_history.clear()



