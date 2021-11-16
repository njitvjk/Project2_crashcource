"""Testing Addition"""
from operations.addition import Addition

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    values = (1.0,2.0)
    addition = Addition(values)
    #Act
    #Assert
    assert addition.get_output() == 3.0
