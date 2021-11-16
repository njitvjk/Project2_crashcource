"""Testing Multiplication"""

from operations.multiplication import Multiplication

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    values = (1.0,2.0)
    multiplication = Multiplication(values)
    #Act
    #Assert
    assert multiplication.get_output() == 2.0
