""" This is class performing operations using the parent and child classes"""

from operations.addition import Addition
from operations.subtraction import Subtraction
from operations.multiplication import Multiplication
from operations.division import Division
class Calculator:
    """ Calculator Class performing operations"""

    @staticmethod
    def add_numbers(value_a, value_b):
        """ Task 9: Add two numbers"""
        addition = Addition(value_a,value_b)
        # return addition.get_output()
        return addition.get_output()

    @staticmethod
    def add_numbers_three_arguments(value_a, value_b,value_c):
        """ Task 9: Add two numbers"""
        addition = Addition(value_a, value_b,value_c)
        return addition.get_output()
    @staticmethod
    def subtract_number(value_a, value_b):
        """ Task 10: Subtract two numbers"""
        subtraction = Subtraction(value_a, value_b)

        return subtraction.get_output()
    @staticmethod
    def multiply_numbers(value_a, value_b):
        """Task 11: Multiply two numbers"""
        multiplication = Multiplication(value_a, value_b)
        return multiplication.get_output()
    @staticmethod
    def divide_numbers(value_a, value_b):
        """ Task 12: Divide two numbers"""
        division=Division(value_a, value_b)
        return division.get_output()

