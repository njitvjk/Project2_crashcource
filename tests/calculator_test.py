"""Tests file """
import logging
import unittest
import pandas as pd
from calculator.calculator import Calculator


def setup_log(name):
    """Log setup """
    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    filename = f"./test_{name}.log"
    log_handler = logging.FileHandler(filename, mode="w")
    log_handler.setLevel(logging.DEBUG)
    log_handler.setFormatter(log_format)

    logger.addHandler(log_handler)
    return logger


class TestApp(unittest.TestCase):
    """Test for Calculator program"""
    # this is the Calculator class instance.

    calculator = None
    df = pd.read_csv('../done/data.csv', sep=',', dtype={
        'OPERATION': str,
        'VALUE_A': float,
        'VALUE_B': float,
        'EXPECTED_OUTPUT': str
    })
    print(df)
    logger = setup_log('debug_calculator')

    def setUp(self):
        self.calculator = Calculator()
        # setup_log('debug_tests')

        print('')
        print('setUp')

    # execute after every test case function run.
    def tearDown(self):
        # release the Calculator object.
        self.calculator = None
        print('')
        print('tearDown')

    def test_0001_add(self):
        """Case1:Addition"""
        print('')
        print('******test_addition******')

        # get each row text from the csv file.

        # the first column in the text line is x value.

        operation = self.df["OPERATION"].iloc[0]
        # the second column in the text line is y value.
        value_x = self.df["VALUE_A"].iloc[0]
        value_y = self.df["VALUE_B"].iloc[0]
        # the third column in the text line is (x + y) value.
        expect_result = self.df["EXPECTED_OUTPUT"].iloc[0]
        # Act
        calc = Calculator()
        result = calc.addition(value_x, value_y)
        # result = self.calculator.plus(x, y)
        print(operation, ':', str(value_x)
              + ' + '
              + str(value_y)
              + ' = '
              + str(result) + ', expect '
              + str(expect_result))
        self.logger.info("Operation %s ,Input file %s ,Record %s,Sum of % s by %s is % s",
                         operation, 'data.csv',
                         self.df[self.df['OPERATION'] == 'ADDITION'].index[0],
                         value_x,
                         value_y,
                         expect_result)
        self.assertEqual(float(result), float(expect_result))

    def test_0002_subtract(self):
        """Case2 :Subtraction"""
        print('')
        print('******test_subtract******')
        operation = self.df["OPERATION"].iloc[1]
        value_x = self.df["VALUE_A"].iloc[1]
        value_y = self.df["VALUE_B"].iloc[1]
        # the third column in the text line is (value_x - y) value.
        expect_result = self.df["EXPECTED_OUTPUT"].iloc[1]
        # result = self.calculator.minus(x, y)
        calc = Calculator()
        result = calc.subtraction(value_x, value_y)

        print(operation, ':', str(value_x) + ' - '
              + str(value_y) + ' = '
              + str(result) + ', expect ' + str(expect_result))
        self.logger.info("Operation %s ,Input file %s ,Record %s,Difference of % s by %s is % s",
                         operation, 'data.csv',
                         self.df[self.df['OPERATION'] == 'SUBTRACTION'].index[0],
                         value_x,
                         value_y,
                         expect_result)
        # Assert
        self.assertEqual(float(result), float(expect_result))

    def test_0003_multiply(self):
        """Case4 :Multiplication"""
        print('')
        print('******test_multiple******')
        operation = self.df["OPERATION"].iloc[2]
        value_x = self.df["VALUE_A"].iloc[2]
        value_y = self.df["VALUE_B"].iloc[2]
        # the third column in the text line is (value_x * value_y) value.
        expect_result = self.df["EXPECTED_OUTPUT"].iloc[2]
        calc = Calculator()
        result = calc.multiplication(value_x, value_y)
        # result = self.calculator.multiple(x, y)

        print(operation, ':',
              str(value_x) + ' * '
              + str(value_y) + ' = '
              + str(result) + ', expect '
              + str(expect_result))
        self.logger.info("Operation %s ,Input file %s ,"
                         "Record %s,"
                         "Product of % s "
                         "by %s is % s",
                         operation, 'data.csv',
                         self.df[self.df['OPERATION'] == 'MULTIPLICATION'].index[0],
                         value_x,
                         value_y,
                         expect_result)

        self.assertEqual(float(result), float(expect_result))

    def test_0004_division(self):
        """Case5 :Division"""
        print('')
        print('******test_divide******')
        operation = self.df["OPERATION"].iloc[3]
        value_x = self.df["VALUE_A"].iloc[3]
        value_y = self.df["VALUE_B"].iloc[3]
        # the sixth column in the text line is (value_x / value_y) value.
        expect_result = self.df["EXPECTED_OUTPUT"].iloc[3]
        calc = Calculator()
        result = calc.division(value_x, value_y)
        print(operation, ':',
              str(value_x) + ' % '
              + str(value_y) + ' = '
              + str(result) + ', expect '
              + str(expect_result))
        self.logger.info("Operation %s ,"
                         "Input file %s ,Record %s,"
                         "Division of % s"
                         " by %s is % s",
                         operation, 'data.csv',
                         self.df[self.df['OPERATION'] == 'DIVISION'].index[0],
                         value_x,
                         value_y,
                         expect_result)
        self.assertEqual(float(result), float(expect_result))

    def test_0005_division_zero(self):
        """Case5 :Division"""
        print('')
        print('******test_divide******')
        operation = self.df["OPERATION"].iloc[4]
        value_x = self.df["VALUE_A"].iloc[4]
        value_y = self.df["VALUE_B"].iloc[4]
        # the sixth column in the text line is (value_x / value_y) value.
        expect_result = self.df["EXPECTED_OUTPUT"].iloc[4]
        calc = Calculator()
        result = calc.division(value_x, value_y)
        print(operation, ':',
              str(value_x) + ' % ' + str(value_y) + ' = '
              + str(result) + ', expect '
              + str(expect_result))
        self.logger.info("Operation %s ,"
                         "Input file %s ,Record %s,Division of % s by %s is % s",
                         operation, 'data.csv',
                         self.df[self.df['OPERATION'] == 'DIVISIONBYZERO'].index[0],
                         value_x,
                         value_y,
                         'INVALID-ATTEMPT TO DIVIDE BY ZERO')
        self.assertEqual(result, expect_result)
        # self.assertRaises(Exception, result)
