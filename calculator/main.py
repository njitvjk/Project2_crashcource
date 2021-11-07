"""Tests file """
import unittest
from calculator.main import Calculator

class TestApp(unittest.TestCase):
    """Test for Calculator program"""
    def setUp(self):
        """Initialization"""
        #Arrange
        self.num_1 = 10
        self.num_2 = 5
    def test_0001_add(self):
        """Case1:Addition"""
        #Act
        calc=Calculator()
        result = calc.addition(self.num_1, self.num_2)
        #Assert
        self.assertEqual(result, 15)
    def test_0002_subtract(self):
        """Case2 :Subtraction"""
        calc = Calculator()
        result = calc.subtraction(self.num_1, self.num_2)
        self.assertEqual(result, 5)
    def test_0003_subtract_negativevalue(self):
        """Case3 :Subtraction_negativeoutput"""
        calc = Calculator()
        result = calc.subtraction(self.num_2, self.num_1)
        self.assertEqual(result, -5)
    def test_0004_multiply(self):
        """Case4 :Multiplication"""
        calc = Calculator()
        result = calc.multiplication(self.num_1, self.num_2)
        self.assertEqual(result, 50)
    def test_0005_division(self):
        """Case5 :Division"""
        calc = Calculator()
        result = calc.division(self.num_1, self.num_2)
        self.assertEqual(result, 2)
    def test_0006_divisionbyzero(self):
        """Case6 :Divisionbyzero"""
        calc=Calculator()
        result = calc.division(1,0)
        self.assertRaises(Exception,result)

if __name__ == '__main__':
    unittest.main()
