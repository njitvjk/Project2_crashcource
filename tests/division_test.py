"""Testing Division"""
from operations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for addition"""
    #Arrange
    values = (100.0,10.0)
    division = Division(values)
    #Act
    #Assert
    assert division.get_output()== 0.1
