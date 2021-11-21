"""Testing the Arithematic operations"""
import pytest

from calculator.calculator import Calculator
from operations.calculator_history import CalculationHistory
@pytest.fixture
def clear_history():
    """fixture function to run before every functions defined below"""
    CalculationHistory.clear_history()
def test_001_add_to_history(clear_history):
    """Case1 :Add calculation to history"""
    Calculator.add_numbers(1, 2)
    Calculator.divide_numbers(5, 1)
    assert CalculationHistory.history_count() == 2
    assert CalculationHistory.get_history() == 5
def test_002_add_values(clear_history):
    """Case1:Add two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(1,2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers_three_arguments(3, 2,1) == 6
    assert Calculator.add_numbers_three_arguments(4, 2,1) == 7
def test_003_clear_history(clear_history):
    """Case2:clear history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(1,2) == 3
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.add_numbers(4, 2) == 6
    assert CalculationHistory.history_count() == 4
    assert CalculationHistory.clear_history() is True
    assert CalculationHistory.history_count() == 0
def test_004_count_history(clear_history):
    """Case3:Count history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert CalculationHistory.history_count() == 0
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert CalculationHistory.history_count() == 2
def test_005_get_first_result(clear_history):
    """Case5: get first result"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert CalculationHistory.get_result_of_first_calculation() == 4
def test_006_subtraction_values(clear_history):
    """Case6:test subtraction"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_number(1, 2) == -1
def test_007_multiplication_values(clear_history):
    """ Case7 :multiplication of two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(1,2) == 2
def test_008_division_values(clear_history):
    """Case9 :Division"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_numbers(2, 2) == 1
def test_009_get_history(clear_history):
    """Case10 :get history returns the last calculation result"""
    # pylint: disable=unused-argument,redefined-outer-name
    Calculator.add_numbers(2, 2)
    Calculator.divide_numbers(2, 2)
    assert CalculationHistory.get_history() ==1
def test_010_get_last_result(clear_history):
    """Case5: get first result"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert CalculationHistory.get_result_of_first_calculation() == 4

