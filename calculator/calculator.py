""" This is class performing operations on Calculations class"""
from history.calculations import Calculations

class Calculator:
    """ Calculator Class performing operations"""
    history = []
    @staticmethod
    def get_last_result_value():
        """  Task 9:This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_result_of_last_calculation()
    @staticmethod
    def add_numbers(tuple_values: tuple):
        """ Task 10: Add two numbers"""
        Calculations.add_addition_calculation(tuple_values)
        return True
    @staticmethod
    def subtract_number(tuple_values: tuple):
        """ Task 11: Subtract two numbers"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True
    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """Task 12: Multiply two numbers"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True
    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ Task 13: Divide two numbers"""
        Calculations.add_division_calculation(tuple_values)
        return True
