"""Calculation history class"""
from operations.addition import Addition
from operations.division import Division
from operations.multiplication import Multiplication
from operations.subtraction import Subtraction
class Calculations:
    """ Methods and attribute to help with history"""
    history=[]
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """ Task 1: clear history"""
        Calculations.history.clear()
        return True
    @staticmethod
    def get_first_calculation():
        """ Task 2: get first calculation"""
        return Calculations.history[0]
    @staticmethod
    def history_count():
        """ Task 3: get history count"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """ Task 4: get last calculation"""
        return Calculations.history[-1]
    @staticmethod
    def get_calculation(num):
        """Task 5:retrieve calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """Task 6:append a calculation to  history"""
        return Calculations.history.append(calculation)
    @staticmethod
    def get_result_of_last_calculation():
        """ Task 7: Get last calculation result"""
        return Calculations.history[-1].get_output()
    @staticmethod
    def get_result_of_first_calculation():
        """ Task 8: Get first calculation result"""
        return Calculations.history[0].get_output()
    @staticmethod
    def add_addition_calculation(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        # Get the result of the calculation
        return True
    @staticmethod
    def add_subtraction_calculation(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True
    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True
    @staticmethod
    def add_division_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        return True
