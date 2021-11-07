"""Testing the Calculator"""
from calculator.main import Calculator
#Arrange
NUM1=5
NUM2=10

def calculator_result():
    """testing calculator result is 0"""
    #Act
    calc = Calculator()
    #Assert
    assert calc.output == 0

def calculator_add():
    """Testing the Add function of the calculator"""
    #Arrange by instantiating the calc class
    calc = Calculator()
    #Act by calling the method to be tested
    calc.addition(NUM1,NUM2)
    #Assert that the results are correct
    assert calc.output == 15

def calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtraction(NUM2,NUM1)
    assert calc.get_result() == 5

def calculator_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result  = calc.multiplication(NUM1,NUM2)
    assert result == 50

def calculator_divide():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result = calc.division(NUM2, NUM1)
    assert result == 2

def calculator_subtractnegative():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtraction(NUM1,NUM2)
    assert calc.get_result() == -5

def calculator_divisionbyzero(self):
    """Testing division by zero"""
    self.assertRaises(ZeroDivisionError, calculator_divide(), 1, 0)
