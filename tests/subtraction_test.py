"""Testing Subtraction"""
from operations.subtraction import Subtraction

def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    #Arrange
    values = (1.0,2.0)
    subtraction = Subtraction(values)
    #Act
    #Assert
    assert subtraction.get_output() == -3
