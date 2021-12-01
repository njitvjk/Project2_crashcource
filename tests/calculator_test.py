"""Tests file """
import csv
import unittest
import pandas as pd

from pyunitreport import HTMLTestRunner

from calculator.main import Calculator

# test data file path, the file is a csv file.
df = pd.read_csv('../input/data.csv',
                 sep=',', )


# load test data from ./test_data.csv file.
def load_test_data():
    print('open and load data from test_data.csv complete.')


# close and release the test data file object.


def build_test_suite():
    # create unittest.TestSuite object.
    test_suite = unittest.TestSuite()
    print("inside build test suite")
    # add each test function to the test suite object.
    test_suite.addTest(TestApp('test_0001_add'))
    test_suite.addTest(TestApp('test_0002_subtract'))
    test_suite.addTest(TestApp('test_0003_multiply'))
    test_suite.addTest(TestApp('test_0004_division'))
    return test_suite


class TestApp(unittest.TestCase):
    """Test for Calculator program"""

    # this is the Calculator class instance.
    calculator = None

    # class level setup function, execute once only before any test function.
    @classmethod
    def setUpClass(cls):
        load_test_data()
        print('')
        print('setUpClass')

    # execute before every test case function run.
    def setUp(self):
        self.calculator = Calculator()
        print('')
        print('setUp')

    # execute after every test case function run.
    def tearDown(self):
        # release the Calculator object.
        if self.calculator is not None:
            self.calculator = None
        print('')
        print('tearDown')

    def test_0001_add(self):
        """Case1:Addition"""
        print('')
        print('******test_addition******')
        # get each row text from the csv file.

        # the first column in the text line is x value.
        operation = df.loc[0][0]
        # the second column in the text line is y value.
        x = df.loc[0][1]
        y = df.loc[0][2]
        # the third column in the text line is (x + y) value.
        expect_result = df.loc[0][3]
        # Act
        calc = Calculator()
        result = calc.addition(x, y)
        # result = self.calculator.plus(x, y)
        print(operation, ':', str(x) + ' + ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
        # Assert
        self.assertEqual(float(result), float(expect_result))

    def test_0002_subtract(self):
        """Case2 :Subtraction"""
        print('')
        print('******test_subtract******')
        operation = df.loc[1][0]
        x = df.loc[1][1]
        y = df.loc[1][2]
        # the third column in the text line is (x - y) value.
        expect_result = df.loc[1][3]
        # result = self.calculator.minus(x, y)
        calc = Calculator()
        result = calc.subtraction(x, y)

        print(operation, ':', str(x) + ' - ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
        self.assertEqual(float(result), float(expect_result))

    def test_0003_multiply(self):
        """Case4 :Multiplication"""
        print('')
        print('******test_multiple******')
        operation = df.loc[2][0]
        x = df.loc[2][1]
        y = df.loc[2][2]
        # the third column in the text line is (x * y) value.
        expect_result = df.loc[2][3]
        calc = Calculator()
        result = calc.multiplication(x, y)
        # result = self.calculator.multiple(x, y)

        print(operation, ':', str(x) + ' * ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
        self.assertEqual(float(result), float(expect_result))

    def test_0004_division(self):
        """Case5 :Division"""
        print('')
        print('******test_divide******')
        operation = df.loc[3][0]
        x = df.loc[3][1]
        y = df.loc[3][2]
        # the sixth column in the text line is (x / y) value.
        expect_result = df.loc[3][3]
        calc = Calculator()
        result = calc.division(x, y)
        print(operation, ':', str(x) + ' % ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
        self.assertEqual(float(result), float(expect_result))

    def test_0005_division_zero(self):
        """Case5 :Division"""
        print('')
        print('******test_divide******')
        operation = df.loc[4][0]
        x = df.loc[4][1]
        y = df.loc[4][2]
        # the sixth column in the text line is (x / y) value.
        expect_result = df.loc[4][3]
        calc = Calculator()
        result = calc.division(x, y)
        print(operation, ':', str(x) + ' % ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
        self.assertRaises(Exception, result)


kwargs = {
    "output": 'reports',
    "report_name": 'report_name',
    "failfast": True

}
report_result = HTMLTestRunner(**kwargs).run(build_test_suite())
