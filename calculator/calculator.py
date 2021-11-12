""" This is class performing operations using the parent and child classes"""

from operations.addition import Addition
from operations.subtraction import Subtraction
from operations.multiplication import Multiplication
from operations.division import Division
class Calculator:
    """ Calculator Class performing operations"""
    history = []

    @staticmethod
    def get_history():
        """ Task 1:get history"""
        return Calculator.history[-1].get_output()
    @staticmethod
    def get_result_of_first_calculation():
        """ Task 2: Get first calculation result"""
        return Calculator.history[0].get_output()
    @staticmethod
    def clear_history():
        """ Task 3: clear history"""
        Calculator.history.clear()
        return True
    @staticmethod
    def history_count():
        """ Task 4: count history"""
        return len(Calculator.history)
    @staticmethod
    def add_calculation_to_history(calculation):
        """ Task 5: add calculation to history"""
        Calculator.history.append(calculation)
        return True
    @staticmethod
    def get_result_of_last_calculation():
        """ Task 6: Get last calculation result"""
        return Calculator.history[-1].get_output()
    @staticmethod
    def get_last_calculation():
        """ Task 7: returns last calculation result"""
        return Calculator.history[-1].get_output()
    @staticmethod
    def get_last_calculation_object():
        """ Task 8: returns last calculation result"""
        return Calculator.history[-1].get_output()
    @staticmethod
    def add_numbers(value_a, value_b):
        """ Task 9: Add two numbers"""
        addition = Addition.create(value_a,value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation()
    @staticmethod
    def subtract_number(value_a, value_b):
        """ Task 10: Subtract two numbers"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation()
    @staticmethod
    def multiply_numbers(value_a, value_b):
        """Task 11: Multiply two numbers"""
        Calculator.add_calculation_to_history(Multiplication.create(value_a,value_b))
        return Calculator.get_result_of_last_calculation()
    @staticmethod
    def divide_numbers(value_a, value_b):
        """ Task 12: Divide two numbers"""
        Calculator.add_calculation_to_history(Division.create(value_a,value_b))
        return Calculator.get_result_of_last_calculation()
